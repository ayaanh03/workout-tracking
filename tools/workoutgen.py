#!/usr/bin/env python3
"""Generate Apple Workout app `.workout` files (WorkoutKit custom workouts).

The format is protobuf. Reverse-engineered layout (field numbers):

  File
    9    string   plan UUID (uppercase)
    11   Workout
    1000 varint   = 1   (constant; format/version marker)
    1002 varint   = 5   (constant; format/version marker)

  Workout
    1  varint   activity type (HKWorkoutActivityType; 37 = running)
    2  varint   location (3 = outdoor)
    3  string   display name
    4  Step     warmup
    5  Block    repeated; every standalone step is its own block (iterations 1)
    6  Step     cooldown

  Block:        1 IntervalStep (repeated), 2 varint iterations
  IntervalStep: 1 varint purpose (1 = work, 2 = recovery), 2 Step
  Step:         1 Goal, 2 Alert (optional)
  Goal:         1 varint type (1 = time, 3 = distance, 4 = open)
                2 Quantity time      (unit 1 = seconds, 2 = minutes)
                4 Quantity distance  (unit 1 = meters, 2 = km, 5 = miles)
  Quantity:     1 varint unit, 2 double value

  Alert:        1 varint kind  (1 = average pace, 2 = current pace,
                                3 = current cadence, 4 = current power,
                                5 = heart rate, 6 = average power)
                2 varint shape (1 = single target, 2 = range, 3 = HR zone)
                4 pace / 5 cadence / 6 power / 7 heart rate payload:
                  single -> { 1 Value }   range -> { 2 { 1 Value lo, 2 Value hi } }
                  zone   -> { 1 { 1 varint zone 1-5 } }
  Values:
    pace     { 1 Quantity distance (m), 2 Quantity time (1 s) }   i.e. m/s;
             range lo is the slower speed
    cadence  { 1 varint steps, 2 Quantity time (1 min) }
    power    Quantity (unit 1 = watts)
    heart    { 1 double bpm }

No dependencies: hand-rolled protobuf writer, so output is byte-for-byte
deterministic. The UUID is derived from the content unless given explicitly.

Spec format (indentation marks repeat members; `#` starts a comment):

    name: 10/07
    warmup: open                 # open | 5:00 | 300s | 5min | 1mi | 2km | 400m
    repeat 3
      work: 1mi @ 7:40/mi        # average pace: 7:40/mi, 4:45/km, 9:10-10:30/mi
      work: 1mi @ current 7:40/mi  # current pace
      recovery: 1:30
    work: 0.25mi @ 120-150bpm    # heart rate range
    work: 0.25mi @ zone 3        # heart rate zone 1-5
    work: 0.25mi @ 170spm        # current cadence: 170spm, 160-190spm
    work: 0.25mi @ 200-205w      # average power (range)
    work: 0.25mi @ current 200w  # current power (single)
    cooldown: open
"""
import argparse
import re
import struct
import sys
import uuid

RUNNING = 37
OUTDOOR = 3
WORK, RECOVERY = 1, 2
GOAL_TIME, GOAL_DISTANCE, GOAL_OPEN = 1, 3, 4
TIME_UNITS = {"s": 1, "min": 2}
DIST_UNITS = {"m": 1, "km": 2, "mi": 5}
METERS_PER = {"mi": 1609.344, "km": 1000.0}
UUID_NAMESPACE = uuid.UUID("6f0d3c1e-2b9a-4c55-9a4e-5f0b8f6a7c21")

# alert kind -> (alert field 1, payload field, shapes seen in real exports)
ALERTS = {
    "avg_pace":     (1, 4, {"single", "range"}),
    "current_pace": (2, 4, {"single", "range"}),
    "cadence":       (3, 5, {"single", "range"}),
    "current_power": (4, 6, {"single"}),
    "hr":            (5, 7, {"range", "zone"}),
    "avg_power":     (6, 6, {"range"}),
}
ALERT_BY_ID = {v[0]: k for k, v in ALERTS.items()}
PACE_KINDS = ("avg_pace", "current_pace")
POWER_KINDS = ("avg_power", "current_power")
SHAPES = {"single": 1, "range": 2, "zone": 3}


# --- protobuf writer -------------------------------------------------------

def _varint(n):
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        if n:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def f_varint(field, n):
    return _varint(field << 3) + _varint(n)


def f_double(field, x):
    return _varint(field << 3 | 1) + struct.pack("<d", x)


def f_bytes(field, b):
    if isinstance(b, str):
        b = b.encode()
    return _varint(field << 3 | 2) + _varint(len(b)) + b


# --- model -> bytes --------------------------------------------------------

def enc_quantity(unit, value):
    return f_varint(1, unit) + f_double(2, float(value))


def enc_goal(goal):
    kind = goal[0]
    if kind == "open":
        return f_varint(1, GOAL_OPEN)
    _, value, unit = goal
    if kind == "time":
        return f_varint(1, GOAL_TIME) + f_bytes(2, enc_quantity(unit, value))
    if kind == "distance":
        return f_varint(1, GOAL_DISTANCE) + f_bytes(4, enc_quantity(unit, value))
    raise ValueError(goal)


def enc_alert_value(kind, v):
    if kind in PACE_KINDS:  # v = meters per second
        return (f_bytes(1, enc_quantity(DIST_UNITS["m"], v))
                + f_bytes(2, enc_quantity(TIME_UNITS["s"], 1.0)))
    if kind == "cadence":
        return f_varint(1, int(v)) + f_bytes(2, enc_quantity(TIME_UNITS["min"], 1.0))
    if kind in POWER_KINDS:
        return enc_quantity(1, v)
    if kind == "hr":
        return f_double(1, float(v))
    raise ValueError(kind)


def enc_alert(alert):
    kind, values = alert["kind"], alert["values"]
    kind_id, payload_field, _ = ALERTS[kind]
    if alert.get("zone"):
        payload = f_bytes(1, f_varint(1, alert["zone"]))
        shape = SHAPES["zone"]
    elif len(values) == 1:
        payload = f_bytes(1, enc_alert_value(kind, values[0]))
        shape = SHAPES["single"]
    else:
        lo, hi = values
        payload = f_bytes(2, f_bytes(1, enc_alert_value(kind, lo))
                          + f_bytes(2, enc_alert_value(kind, hi)))
        shape = SHAPES["range"]
    return f_varint(1, kind_id) + f_varint(2, shape) + f_bytes(payload_field, payload)


def enc_step(step):
    out = f_bytes(1, enc_goal(step["goal"]))
    if step.get("alert"):
        out += f_bytes(2, enc_alert(step["alert"]))
    return out


def encode(plan, plan_uuid=None):
    w = f_varint(1, RUNNING) + f_varint(2, OUTDOOR) + f_bytes(3, plan["name"])
    if plan.get("warmup"):
        w += f_bytes(4, enc_step(plan["warmup"]))
    for block in plan["blocks"]:
        b = b"".join(
            f_bytes(1, f_varint(1, s["purpose"]) + f_bytes(2, enc_step(s)))
            for s in block["steps"])
        b += f_varint(2, block["iterations"])
        w += f_bytes(5, b)
    if plan.get("cooldown"):
        w += f_bytes(6, enc_step(plan["cooldown"]))
    if plan_uuid is None:
        plan_uuid = str(uuid.uuid5(UUID_NAMESPACE, w.hex()))
    return (f_bytes(9, plan_uuid.upper()) + f_bytes(11, w)
            + f_varint(1000, 1) + f_varint(1002, 5))


# --- bytes -> model (for inspecting files exported from the app) ----------

def _read_varint(b, i):
    r = s = 0
    while True:
        c = b[i]
        i += 1
        r |= (c & 0x7F) << s
        s += 7
        if c < 0x80:
            return r, i


def parse_msg(b, kind=None, known=None):
    """Return {field: [values]}; length-delimited values stay as bytes.

    If `known` is given, any other field number is an error, so new app
    features are flagged instead of silently dropped.
    """
    out, i = {}, 0
    while i < len(b):
        key, i = _read_varint(b, i)
        field, wt = key >> 3, key & 7
        if wt == 0:
            v, i = _read_varint(b, i)
        elif wt == 1:
            v = struct.unpack("<d", b[i:i + 8])[0]
            i += 8
        elif wt == 2:
            n, i = _read_varint(b, i)
            v = b[i:i + n]
            i += n
        elif wt == 5:
            v = struct.unpack("<f", b[i:i + 4])[0]
            i += 4
        else:
            raise ValueError(f"unsupported wire type {wt}")
        out.setdefault(field, []).append(v)
    if known is not None and set(out) - set(known):
        raise ValueError(f"unknown {kind} fields {sorted(set(out) - set(known))}; "
                         "send this sample over")
    return out


def dec_quantity(b):
    m = parse_msg(b, "quantity", {1, 2})
    return m[1][0], m[2][0]


def dec_alert_value(kind, b):
    if kind in PACE_KINDS:
        m = parse_msg(b, "pace value", {1, 2})
        du, dist = dec_quantity(m[1][0])
        tu, secs = dec_quantity(m[2][0])
        assert (du, tu, secs) == (DIST_UNITS["m"], TIME_UNITS["s"], 1.0), (du, tu, secs)
        return dist
    if kind == "cadence":
        m = parse_msg(b, "cadence value", {1, 2})
        assert dec_quantity(m[2][0]) == (TIME_UNITS["min"], 1.0)
        return m[1][0]
    if kind in POWER_KINDS:
        unit, v = dec_quantity(b)
        assert unit == 1, f"power unit {unit}"
        return v
    if kind == "hr":
        return parse_msg(b, "heart rate value", {1})[1][0]
    raise ValueError(kind)


def dec_alert(b):
    a = parse_msg(b, "alert", {1, 2, 4, 5, 6, 7})
    kind = ALERT_BY_ID.get(a[1][0])
    if kind is None:
        raise ValueError(f"unknown alert kind {a[1][0]}; send this sample over")
    payload_field = ALERTS[kind][1]
    if set(a) != {1, 2, payload_field}:
        raise ValueError(f"{kind} alert has fields {sorted(a)}; send this sample over")
    p = parse_msg(a[payload_field][0], "alert payload", {1, 2})
    if a[2][0] == SHAPES["single"] and set(p) == {1}:
        values = [dec_alert_value(kind, p[1][0])]
    elif a[2][0] == SHAPES["range"] and set(p) == {2}:
        r = parse_msg(p[2][0], "alert range", {1, 2})
        values = [dec_alert_value(kind, r[1][0]), dec_alert_value(kind, r[2][0])]
    elif a[2][0] == SHAPES["zone"] and kind == "hr" and set(p) == {1}:
        return {"kind": kind, "values": [],
                "zone": parse_msg(p[1][0], "heart rate zone", {1})[1][0]}
    else:
        raise ValueError(f"unknown alert shape {a[2][0]}; send this sample over")
    return {"kind": kind, "values": values}


def dec_step(b):
    m = parse_msg(b, "step", {1, 2})
    g = parse_msg(m[1][0], "goal", {1, 2, 4})
    t = g[1][0]
    if t == GOAL_OPEN:
        goal = ("open",)
    elif t == GOAL_TIME:
        unit, v = dec_quantity(g[2][0])
        goal = ("time", v, unit)
    elif t == GOAL_DISTANCE:
        unit, v = dec_quantity(g[4][0])
        goal = ("distance", v, unit)
    else:
        raise ValueError(f"unknown goal type {t}; send this sample over")
    return {"goal": goal, "alert": dec_alert(m[2][0]) if 2 in m else None}


def decode(data):
    f = parse_msg(data, "file", {9, 11, 1000, 1002})
    w = parse_msg(f[11][0], "workout", {1, 2, 3, 4, 5, 6})
    if (w[1][0], w[2][0]) != (RUNNING, OUTDOOR):
        raise ValueError(f"activity {w[1][0]} / location {w[2][0]} not mapped yet")
    plan = {"name": w[3][0].decode(), "blocks": [],
            "warmup": dec_step(w[4][0]) if 4 in w else None,
            "cooldown": dec_step(w[6][0]) if 6 in w else None}
    for bb in w.get(5, []):
        bm = parse_msg(bb, "block", {1, 2})
        steps = []
        for sb in bm[1]:
            sm = parse_msg(sb, "interval step", {1, 2})
            s = dec_step(sm[2][0])
            s["purpose"] = sm[1][0]
            steps.append(s)
        plan["blocks"].append({"iterations": bm[2][0], "steps": steps})
    return plan, f[9][0].decode()


# --- spec text <-> model ---------------------------------------------------

def parse_clock(s):
    secs = 0
    for p in s.split(":"):
        secs = secs * 60 + int(p)
    return secs


def parse_alert(text):
    t = text.strip().lower()
    metric = None  # avg | current; pace and power default to avg
    if m := re.fullmatch(r"(avg|current)\s+(.*)", t):
        metric, t = m.group(1), m.group(2)
    if not metric and (m := re.fullmatch(r"(?:hr\s*)?zone\s*([1-5])", t)):
        return {"kind": "hr", "values": [], "zone": int(m.group(1))}
    if m := re.fullmatch(r"(\d+:\d{2})(?:\s*-\s*(\d+:\d{2}))?\s*/\s*(mi|km)", t):
        kind = f"{metric or 'avg'}_pace"
        per = METERS_PER[m.group(3)]
        paces = [parse_clock(g) for g in m.group(1, 2) if g]
        # stored as speeds, slow -> fast
        values = sorted(per / p for p in paces)
    elif m := re.fullmatch(r"(\d+)(?:\s*-\s*(\d+))?\s*(bpm|spm)", t):
        kind = "hr" if m.group(3) == "bpm" else "cadence"
        if metric and not (kind == "cadence" and metric == "current"):
            raise ValueError(f"a {metric} {kind} alert hasn't been seen in a real export yet; "
                             "make one in the app and send it over")
        values = [int(g) for g in m.group(1, 2) if g]
    elif m := re.fullmatch(r"(\d+(?:\.\d+)?)(?:\s*-\s*(\d+(?:\.\d+)?))?\s*w", t):
        kind = f"{metric or 'avg'}_power"
        values = [float(g) for g in m.group(1, 2) if g]
    else:
        raise ValueError(f"can't parse alert {text!r} "
                         "(use 7:40/mi, current 9:10-10:30/mi, 120-150bpm, zone 3, 170spm, 200-205w, current 200w)")
    shape = "single" if len(values) == 1 else "range"
    if kind == "hr" and shape == "single":
        raise ValueError("the app only has heart rate ranges or zones, e.g. 120-150bpm, zone 3")
    if shape not in ALERTS[kind][2]:
        raise ValueError(f"a {shape} {kind} alert hasn't been seen in a real export yet; "
                         "make one in the app and send it over")
    return {"kind": kind, "values": values}


def parse_step_spec(text):
    text = text.strip()
    alert = None
    if "@" in text:
        text, a = text.split("@", 1)
        text, alert = text.strip(), parse_alert(a)
    if text == "open":
        goal = ("open",)
    elif m := re.fullmatch(r"(\d+(?:\.\d+)?)\s*(mi|km|m)", text):
        goal = ("distance", float(m.group(1)), DIST_UNITS[m.group(2)])
    elif m := re.fullmatch(r"(\d+(?:\.\d+)?)\s*(s|min)", text):
        goal = ("time", float(m.group(1)), TIME_UNITS[m.group(2)])
    elif re.fullmatch(r"\d+(:\d{2}){1,2}", text):
        goal = ("time", parse_clock(text), TIME_UNITS["s"])
    else:
        raise ValueError(f"can't parse goal {text!r} "
                         "(use open, 1mi, 2km, 400m, 1:30, 90s, 5min)")
    return {"goal": goal, "alert": alert}


def parse_spec(src):
    plan = {"name": None, "warmup": None, "cooldown": None, "blocks": []}
    current = None  # block being filled by an indented `repeat`
    for lineno, raw in enumerate(src.splitlines(), 1):
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indented = line[0] in " \t"
        line = line.strip()
        try:
            if m := re.fullmatch(r"repeat\s+(\d+)", line):
                current = {"iterations": int(m.group(1)), "steps": []}
                plan["blocks"].append(current)
                continue
            key, _, val = line.partition(":")
            key = key.strip().lower()
            if not indented:
                current = None
            if key == "name":
                plan["name"] = val.strip()
            elif key in ("warmup", "cooldown"):
                plan[key] = parse_step_spec(val)
            elif key in ("work", "recovery"):
                step = parse_step_spec(val)
                step["purpose"] = WORK if key == "work" else RECOVERY
                if current is not None:
                    current["steps"].append(step)
                else:
                    plan["blocks"].append({"iterations": 1, "steps": [step]})
            else:
                raise ValueError(f"unknown key {key!r}")
        except ValueError as e:
            raise SystemExit(f"line {lineno}: {e}")
    if not plan["name"]:
        raise SystemExit("spec needs a `name:` line")
    return plan


def fmt_clock(secs):
    h, rem = divmod(int(secs), 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def fmt_pace(mps):
    # Pick the unit whose pace comes out to whole seconds, so specs round-trip.
    for unit in ("mi", "km"):
        secs = METERS_PER[unit] / mps
        if abs(secs - round(secs)) < 1e-6 and METERS_PER[unit] / round(secs) == mps:
            return fmt_clock(round(secs)), unit
    raise ValueError(f"pace {mps} m/s isn't a whole-second pace per mi or km")


def fmt_alert(alert):
    kind, values = alert["kind"], alert["values"]
    if alert.get("zone"):
        return f"zone {alert['zone']}"
    if kind in PACE_KINDS:
        parts = [fmt_pace(v) for v in reversed(values)]  # fast -> slow reads naturally
        unit = parts[0][1]
        out = "-".join(p for p, _ in parts) + f"/{unit}"
        return f"current {out}" if kind == "current_pace" else out
    suffix = {"hr": "bpm", "cadence": "spm"}.get(kind, "w")
    out = "-".join(f"{v:g}" for v in values) + suffix
    return f"current {out}" if kind == "current_power" else out


def fmt_step(step):
    g = step["goal"]
    if g[0] == "open":
        out = "open"
    elif g[0] == "time":
        _, v, unit = g
        if unit == TIME_UNITS["s"] and v == int(v):
            out = fmt_clock(v)
        else:
            out = f"{v:g}{ {1: 's', 2: 'min'}[unit] }"
    else:
        unit = {v: k for k, v in DIST_UNITS.items()}[g[2]]
        out = f"{g[1]:g}{unit}"
    if step.get("alert"):
        out += f" @ {fmt_alert(step['alert'])}"
    return out


def to_spec(plan):
    lines = [f"name: {plan['name']}"]
    if plan["warmup"]:
        lines.append(f"warmup: {fmt_step(plan['warmup'])}")
    for b in plan["blocks"]:
        indent = ""
        if b["iterations"] != 1:
            lines.append(f"repeat {b['iterations']}")
            indent = "  "
        for s in b["steps"]:
            kind = "work" if s["purpose"] == WORK else "recovery"
            lines.append(f"{indent}{kind}: {fmt_step(s)}")
    if plan["cooldown"]:
        lines.append(f"cooldown: {fmt_step(plan['cooldown'])}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="spec file -> .workout")
    b.add_argument("spec")
    b.add_argument("-o", "--out", help="output path (default: <spec name>.workout)")
    b.add_argument("--uuid", help="force a plan UUID (default: derived from content)")
    d = sub.add_parser("decode", help=".workout -> spec text")
    d.add_argument("files", nargs="+")
    args = ap.parse_args()

    if args.cmd == "build":
        with open(args.spec) as fh:
            plan = parse_spec(fh.read())
        out = args.out or re.sub(r"\.[^.]*$", "", args.spec) + ".workout"
        with open(out, "wb") as fh:
            fh.write(encode(plan, args.uuid))
        print(out)
    else:
        for path in args.files:
            with open(path, "rb") as fh:
                plan, plan_uuid = decode(fh.read())
            print(f"# {path}  uuid={plan_uuid}")
            sys.stdout.write(to_spec(plan))


if __name__ == "__main__":
    main()
