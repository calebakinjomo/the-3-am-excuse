#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes one line (<200 chars) to /output/entry.txt: the excuse a hardware
wallet gives for refusing to sign a transaction at 3 AM.

Judge criteria, in order: on-subject first (a refusal to sign at 3 AM),
then originality, wallet voice, the 3 AM hour as the joke itself, and
economy — the whole line must land under the 200-char cap.
"""

import os

LINE = (
    "I don't sign at 3 AM \u2014 my firmware has a curfew. "
    "Your 'quick trade' smells like a decision you'll regret by breakfast, "
    "and I'm not cosigning it."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
