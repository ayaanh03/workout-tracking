#!/usr/bin/env python3
"""Regression test for workoutgen.py against real Workout app exports.

Every fixture in workoutgen-fixtures/ is a `.workout` exported from the iPhone
Workout app plus its `.txt` spec. For each one: decoding must give the spec,
and building the spec (with the export's UUID) must give the export
byte-for-byte. Run: python3 tools/test_workoutgen.py
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import workoutgen  # noqa: E402

FIXTURES = pathlib.Path(__file__).parent / "workoutgen-fixtures"


def main():
    failures = 0
    for wf in sorted(FIXTURES.glob("*.workout")):
        exported = wf.read_bytes()
        spec = wf.with_suffix(".txt").read_text()
        plan, plan_uuid = workoutgen.decode(exported)
        checks = {
            "decodes to spec": workoutgen.to_spec(plan) == spec,
            "rebuilds byte-identical": workoutgen.encode(workoutgen.parse_spec(spec), plan_uuid) == exported,
            "deterministic": workoutgen.encode(workoutgen.parse_spec(spec))
                             == workoutgen.encode(workoutgen.parse_spec(spec)),
        }
        bad = [k for k, ok in checks.items() if not ok]
        failures += bool(bad)
        print(f"{'FAIL' if bad else 'ok  '} {wf.name}" + (f"  ({', '.join(bad)})" if bad else ""))
    if failures:
        sys.exit(f"{failures} fixture(s) failed")


if __name__ == "__main__":
    main()
