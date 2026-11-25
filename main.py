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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
