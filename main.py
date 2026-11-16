#!/usr/bin/env python3
"""Copy the entry image to /output/entry.png, deterministically.

The image is a fixed file shipped in this repository; this program only
copies its bytes to the output path, so repeated runs are byte-identical.
Standard library only.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "image.jpg")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
