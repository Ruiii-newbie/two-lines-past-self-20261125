#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Writes the two entry lines to /output/entry.txt (UTF-8, exactly two lines).
Line 1 warns my past self about one specific moment; line 2 says why that
moment mattered and what changed because of it.

Pure standard library, no I/O besides the output file, fully deterministic.
"""

import os
import re

OUTPUT_PATH = "/output/entry.txt"

LINE_ONE = (
    "When the recruiter calls at 4 p.m. on the last Friday in March and "
    "offers you the safe job with the corner office, tell him you need "
    "the weekend to think."
)

LINE_TWO = (
    "That weekend is the only reason you ever built anything of your own, "
    "because the safe job would have paid for the apartment and quietly "
    "bought the rest of your twenties."
)

ENTRY_LINES = (LINE_ONE, LINE_TWO)


def render(lines):
    """Join the lines with newlines and end the file with one newline.

    Guard the gate before writing: exactly two non-empty lines, each a
    single sentence ending in a full stop.
    """
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines")
    for line in lines:
        if not line.strip():
            raise ValueError("entry lines must not be empty")
        # One sentence: no sentence boundary (terminator + space + capital)
        # inside the line, and it must end with a full stop. Abbreviations
        # such as "p.m." do not count: the word after them is lowercase.
        parts = re.split(r"(?<=[.!?])\s+(?=[A-Z])", line.strip())
        if len(parts) != 1 or not line.rstrip().endswith("."):
            raise ValueError("each entry line must be one sentence")
    return "\n".join(lines) + "\n"


def main():
    text = render(ENTRY_LINES)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
