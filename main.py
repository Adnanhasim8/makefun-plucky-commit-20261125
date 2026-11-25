#!/usr/bin/env python3
"""Write the 3 AM commit message entry to /output/entry.txt.

Standard library only, no network at run time.
"""

import os

ENTRY = "fix: at 3 AM I restored prod from a backup I hallucinated"


def main() -> None:
    # Gate assertions: the entry must be exactly one line, 1-200
    # characters, non-empty (no trailing newline written).
    assert ENTRY, "entry must not be empty"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry must match exactly"
    assert "\n" not in written and 1 <= len(written) <= 200


if __name__ == "__main__":
    main()
