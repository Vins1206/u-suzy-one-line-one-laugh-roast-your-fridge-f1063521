"""One-line fridge roast for make.fun.

Writes exactly one line of plain text, at most 200 characters,
to /output/entry.txt -- just the roast itself, nothing else.
Python standard library only; deterministic.
"""

import os

LINE = "My fridge treats the crisper drawer like a witness protection program: the lettuce goes in crisp, comes out unrecognizable, and never talks again."


def main():
    # Gate: exactly one line, 1-200 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200, "roast must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "roast must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
