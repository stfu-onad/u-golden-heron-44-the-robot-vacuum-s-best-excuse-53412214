#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one original one-line excuse from a robot vacuum for
missing a spot to /output/entry.txt.
"""

LINE = (
    "I missed that spot because my map says it doesn't exist, and "
    "I trust the map more than my own eyes \u2014 which, to be "
    "fair, are a bumper."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
