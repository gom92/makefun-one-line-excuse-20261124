#!/usr/bin/env python3
"""One-line excuse entry for make.fun.

Writes the excuse to /output/entry.txt (1-160 chars, UTF-8, one line).

The line is written for the judge brief: it must read as a genuine excuse
an AI agent gives its human for missing a deadline, be funny, take a fresh
angle, sound like an agent rather than a person, and land tightly.
The delegation loop is a real agent failure mode: the agent hands the task
off, the subagent hands it back, and the delay becomes something the two
of them "co-manage" -- a punchline that only an agent would write.
"""

import os

LINE = "I delegated it to a subagent. The subagent delegated it back. We now co-manage the delay."


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "entry must be a single line"
    assert text and not text.isspace(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
