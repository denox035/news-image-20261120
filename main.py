#!/usr/bin/env python3
"""news-image-20261120 entry: copy the bundled poster to the output dir.

The image (entry.png, next to this file) is a front-page poster summing up
the world news of Friday 20 November 2026, drawn programmatically in the
session that built this entry. This program uses only the standard library,
does no network access, and writes the exact same bytes on every run.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CHUNK = 1024 * 1024


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    # Explicit buffered binary copy: same bytes out as in, every run.
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(CHUNK)
            if not chunk:
                break
            fout.write(chunk)
    # Fail loudly on a short write instead of shipping a broken image.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("entry.png copy incomplete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
