#!/usr/bin/env python3
"""Dashboard behavior checks. Requires Python Playwright and Chromium.

Run: python tools/test_dashboard.py
Set DASHBOARD_BROWSER if Chromium is not on PATH. No network server is needed;
requests are served from repository files and isolated in-memory test fixtures.
"""
import copy
import json
import os
from pathlib import Path
import shutil
import unittest
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def actual(slot, exercise, sets, status='completed', note=None):
    result = {'slotId': slot, 'exercise': exercise, 'status': status,
              'sets': [{'load': w, 'units': 'bodyweight' if w == 'BW' else 'lb',
                        'reps': n, 'rir': r} for w, n, r in sets]}
    if note:
        result['note'] = note
    return result


def session(date, name, exercises):
    return {'date': date, 'week': 'W1', 'stage': 'A', 'sessionName': name,
            'sessionId': 'test-' + date, 'prescriptionId': 'test-plan-' + date,
            'exercises': exercises}


HISTORY = {'schemaVersion': 1, 'blockId': 'dashboard-test', 'sessions': [
    session('2026-10-29', 'Upper B', [
        actual('T5', 'Cable pushdown', [(50, 12, 3)]),
        actual('T7', 'Ab circuit — bodyweight', [], 'substituted',
               'Decline crunch skipped. BW plank120 seconds and leg raises; total set count unreported.')]),
    session('2026-10-31', 'Delts/arms B', [
        actual('S2', 'Incline DB curl', [(25, 9, 3)]),
        actual('S3', 'Overhead cable triceps extension', [(35, 10, 3)])]),
    session('2026-11-01', 'Legs', [
        actual('L4', 'Seated leg curl', [(85, 12, 5), (100, 10, 3)])]),
    session('2026-11-02', 'Upper A', [
        actual('M1b', 'Incline barbell bench — back-offs', [(135, 8, 3), (135, 8, 3)]),
        actual('M2', 'Incline DB curl', [(22.5, 12, 3), (22.5, 8, 3)]),
        actual('M4', 'Cable pushdown', [(50, 12, 3), (50, 12, 2)]),
        actual('M6', 'Decline crunch — bodyweight', [('BW', 15, 10), ('BW', 15, 3)])])
]}


def brief():
    rows = [
        ('M1b', 'Incline barbell bench — back-offs', '2×6–8', '135 lb', '2–3', '3 min'),
        ('M2', 'Incline DB curl', '2×12/8', '22.5 lb', '3', '2 min'),
        ('M4', 'Cable pushdown', '2×10–15', '50 lb', '2–3', '2 min'),
        ('S3', 'Cable pushdown', '2×10–15', '50 lb', '2–3', '2 min'),
        ('T7', 'Decline crunch — bodyweight', '2×10–15', 'BW', '3', '2 min')]
    table = [dict(zip(('slotId', 'exercise', 'setsReps', 'load', 'rir', 'rest'), r)) for r in rows]
    table[1]['repTargets'] = [12, 8]
    return {'blockId': 'dashboard-test', 'date': '2026-11-09', 'day': 'Mon', 'week': 'W3',
            'generatedAt': '2026-11-09T10:00:00-05:00', 'sessionName': 'Upper A',
            'prescriptionId': 'test-current-plan', 'preview': False, 'lift': {'table': table},
            'currentLoads': [], 'cardio': None}


class DashboardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pw = sync_playwright().start()
        executable = os.environ.get('DASHBOARD_BROWSER') or shutil.which('chromium') or shutil.which('chromium-browser')
        cls.browser = cls.pw.chromium.launch(**({'executable_path': executable} if executable else {}),
                                           args=['--no-sandbox'])

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.pw.stop()

    def page(self, data=None, missing_history=False, mobile=True):
        page = self.browser.new_page(viewport={'width': 390 if mobile else 1100, 'height': 844})
        page.set_default_timeout(5000)
        self.addCleanup(page.close)
        errors = []
        page.on('pageerror', lambda e: errors.append(str(e)))

        def route(request):
            name = urlparse(request.request.url).path.lstrip('/')
            if data is not None and name == 'latest-workout.json':
                request.fulfill(json=data)
            elif name == 'lifting-history.json' and missing_history:
                request.fulfill(status=404, body='missing')
            elif data is not None and name == 'lifting-history.json':
                request.fulfill(json=HISTORY)
            else:
                path = ROOT / name
                if path.is_dir():
                    path /= 'index.html'
                request.fulfill(path=str(path)) if path.exists() else request.fulfill(status=404, body='missing')

        page.route('http://workout.test/**', route)
        page.goto('http://workout.test/', wait_until='networkidle')
        self.assertEqual(errors, [])
        self.addCleanup(lambda: self.assertEqual(errors, []))
        return page

    def test_real_history_order_and_current_actuals(self):
        history = json.loads((ROOT / 'lifting-history.json').read_text())
        state = json.loads((ROOT / 'state/lifting.json').read_text())
        self.assertEqual(len({s['sessionId'] for s in history['sessions']}), len(history['sessions']))
        for slot, record in state['slots'].items():
            record = record.get('temporary_substitution', record)
            last = record.get('last_actual')
            if not last:
                continue
            matches = [ex for s in history['sessions'] if s['date'] == last['date']
                       for ex in s['exercises'] if ex['slotId'] == slot and ex['status'] == 'completed']
            self.assertEqual(len(matches), 1, slot)
            sets = [{k: s[k] for k in ('load', 'reps', 'rir')} for s in matches[0]['sets']]
            expected = [{k: s[k] for k in ('load', 'reps', 'rir')} for s in last['sets']]
            # Existing pull-up convention records0 added load; the display explicitly usesBW.
            if slot == 'T4':
                for s in expected:
                    if s['load'] == 0:
                        s['load'] = 'BW'
            self.assertEqual(sets, expected, slot)
        page = self.page()
        self.assertEqual(page.locator('.history-session').count(), len(history['sessions']))
        self.assertEqual(page.locator('.loads tbody tr').count(), len(state['slots']))
        self.assertEqual(page.locator('.load-group').count(), 5)
        for selector in ['.history', '.load-reference']:
            self.assertTrue(page.evaluate('(s)=>!!(document.querySelector(s).compareDocumentPosition(document.querySelector(".week")) & Node.DOCUMENT_POSITION_FOLLOWING)', selector))
        self.assertTrue(page.evaluate('document.documentElement.scrollWidth <= innerWidth'))

    def test_unknown_circuit_and_mixed_loads_are_not_invented(self):
        page = self.page(brief())
        circuit = page.locator('[data-session-id="test-2026-10-29"]')
        circuit.locator('summary').click()
        self.assertIn('1 recorded set', circuit.locator('summary').inner_text())
        self.assertIn('Substituted; set count unreported', circuit.inner_text())
        self.assertIn('120 seconds', circuit.inner_text())
        legs = page.locator('[data-session-id="test-2026-11-01"]')
        legs.locator('summary').click()
        self.assertIn('85 lb × 12 · RIR 5', legs.inner_text())
        self.assertIn('100 lb × 10 · RIR 3', legs.inner_text())

    def test_same_slot_history_rest_and_explicit_rep_targets(self):
        page = self.page(brief(), mobile=False)
        boxes = page.locator('.log-ex')
        self.assertIn('Rest 3 min between sets', boxes.nth(0).inner_text())
        self.assertIn('2026-11-02', boxes.nth(1).locator('.last-performance').inner_text())
        self.assertIn('22.5 lb × 12 · RIR 3', boxes.nth(1).inner_text())
        self.assertNotIn('25 lb × 9', boxes.nth(1).inner_text())
        self.assertIn('50 lb × 12', boxes.nth(2).inner_text())
        self.assertIn('No earlier result', boxes.nth(3).inner_text())  # Different exercise / no T5 transfer.
        self.assertIn('No earlier result', boxes.nth(4).inner_text())  # Circuit is not crunch history.
        reps = boxes.nth(1).locator('.set:not(.set-head) input:nth-of-type(2)')
        self.assertEqual([reps.nth(i).input_value() for i in range(2)], ['', ''])
        self.assertEqual([reps.nth(i).get_attribute('placeholder') for i in range(2)], ['12', '8'])
        boxes.nth(1).get_by_role('button', name='Confirm exact targets').click()
        self.assertEqual([reps.nth(i).input_value() for i in range(2)], ['12', '8'])
        self.assertTrue(page.evaluate('document.documentElement.scrollWidth <= innerWidth'))

    def test_saved_draft_survives_changed_prescription_without_new_references(self):
        data = brief()
        page = self.page(data)
        box = page.locator('.log-ex').nth(1)
        box.locator('.set:not(.set-head) input:nth-of-type(2)').first.fill('9')
        draft = page.evaluate("JSON.parse(localStorage.getItem('liftlog:2026-11-09'))")
        # Same exercise, different older load/rest still counts as a stale prescription.
        prior = copy.deepcopy(data['lift']['table'])
        prior[1].update(load='20 lb', rest='3 min')
        draft['prescription'] = json.dumps(prior, ensure_ascii=False, separators=(',', ':'))
        page.evaluate("d=>localStorage.setItem('liftlog:2026-11-09',JSON.stringify(d))", draft)
        page.reload(wait_until='networkidle')
        self.assertIn('older prescription', page.inner_text('body'))
        self.assertEqual(page.locator('.log-ex').nth(1).locator('.set:not(.set-head) input:nth-of-type(2)').first.input_value(), '9')
        self.assertEqual(page.locator('.log .rest-time').count(), 0)
        self.assertEqual(page.locator('.log .last-performance').count(), 0)
        self.assertEqual(page.evaluate("JSON.parse(localStorage.getItem('liftlog:2026-11-09'))"), draft)

    def test_completed_same_date_and_missing_history(self):
        data = brief()
        data.update(date='2026-11-02', status='done')
        page = self.page(data)
        self.assertEqual(page.locator('.log').count(), 0)
        page = self.page({**data, 'status': None})
        self.assertIn('No earlier result', page.locator('.log-ex').nth(1).inner_text())
        page = self.page(brief(), missing_history=True)
        self.assertEqual(page.locator('.history').count(), 0)
        self.assertEqual(page.locator('.week').count(), 1)
        self.assertEqual(page.locator('.log .rest-time').count(), 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
