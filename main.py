#!/usr/bin/env python3
"""One Line, One Chill entry: a single sentence of horror.

Writes the entry to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""
import os
import stat

ENTRY = (
    "The doorbell camera caught me leaving at 02:47, but I have not left "
    "the house in three days, and the man on the porch is wearing my coat."
)


def main():
    # Gate: /output/entry.txt must be UTF-8, 1-200 characters, not only
    # whitespace, and a single sentence of horror.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
