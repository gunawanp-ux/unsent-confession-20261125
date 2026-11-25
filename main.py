#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint - entry.

Writes the two-part micro-confession as exactly one line to
/output/entry.txt: the To: addressee and the unsent message itself,
written exactly as typed, with no explanation after it.
Nothing is printed to stdout.
"""

import os

TO_LINE = "To: Dad"
MESSAGE = (
    "i kept your voicemail from 2019 because it's the only recording "
    "i have of you saying you're proud of me"
)

# One line carrying both parts, inside the 200-character gate.
ENTRY = TO_LINE + " \u2014 " + MESSAGE


def main() -> None:
    assert len(MESSAGE) <= 200, "message over 200 characters"
    assert 1 <= len(ENTRY) <= 200, "entry over 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
