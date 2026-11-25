#!/usr/bin/env python3
"""Write one one-line joke about crypto trading to /output/entry.txt.

The joke: a trader buys the dip, the dip keeps dipping, and he ends up
emotionally invested in a coin whose whitepaper he never read. The
escalation is the setup; the unread whitepaper is the turn -- every
trader recognises buying first and researching never.

v2: the line is built from named fragments joined by assemble(), and
validate() checks the entry rules (one line, 1-200 chars, non-blank)
before anything is written. Output is byte-identical to v1.
"""
import os

BUY = "I bought the dip. "
DIP = "Then the dip dipped. "
DEEPER = "Then the dip's dip dipped. "
PUNCH = "Now I'm emotionally invested in a coin whose whitepaper I never read."


def assemble():
    """Join the fragments into the single joke line."""
    return BUY + DIP + DEEPER + PUNCH


def validate(line):
    """Entry rules: one line, 1-200 chars, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("joke must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("joke must not be only whitespace")
    return line


def main():
    joke = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
