#!/usr/bin/env python3
"""The Funniest Out-of-Office — writes one line to /output/entry.txt.

The line is a one-line out-of-office auto-reply a real person could set:
I'm on holiday, and my inbox is being watched by my fridge — which only
answers emails about snacks and has already accepted two meetings. The
joke turns on the surprise that the "colleague" covering my inbox is a
kitchen appliance with snack-only priorities, and the deadpan kicker that
it has already accepted meetings, so the auto-reply itself is failing
upwards while I'm away.
"""

import os

LINE = "I'm on holiday until Monday. My inbox is watched by my fridge, which only answers emails about snacks and has accepted two meetings."

# Gate guard: the sealed scorer only accepts a single non-blank line of
# 1 to 140 characters; fail loudly here instead of shipping an invalid entry.
assert 1 <= len(LINE) <= 140 and "\n" not in LINE and LINE.strip(), "entry violates the gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
