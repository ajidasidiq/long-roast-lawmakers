#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one original satirical sentence to /output/entry.txt.
The sentence sets up the lawmakers' authority (a 400-page AI law)
and undercuts it with the file they cannot convert: the bill itself.
"""

import os
import sys

ENTRY = (
    "They passed a 400-page law to govern artificial intelligence, "
    "then asked the intern how to turn the bill itself into a PDF."
)

MAX_CHARS = 140


def gate_check(text: str) -> None:
    """Self-check mirroring the competition gate: one line, 1-140 chars.

    Also enforces the judge's shape: exactly one sentence, so the punch
    lands once, on the last few words, with nothing after it.
    """
    if not text or not text.strip():
        raise SystemExit("gate failed: entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"gate failed: entry is {len(text)} chars, over {MAX_CHARS}"
        )
    if len(text) < 1:
        raise SystemExit("gate failed: entry is empty")
    # One sentence only: a single terminal period, at the very end.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("gate failed: entry must be exactly one sentence")
    if text != text.strip():
        raise SystemExit("gate failed: entry has leading/trailing whitespace")


def main() -> None:
    gate_check(ENTRY)
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {out_path}")


if __name__ == "__main__":
    main()
