#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — entry program.

Writes the GPS's own one-line excuse to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Standard library only.
No trailing newline; exactly one line, 1-200 characters.
"""

import os

ENTRY = "The bridge filed for divorce, the lake got the road in the settlement, and I just follow the paperwork."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
