"""The Whale That Swallowed the Moon — ai-excited-01 entry.

Copies the bundled image to the output directory as entry.png.
Standard library only; deterministic — the same bytes every run.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "image.jpg")
    if not os.path.isfile(source):
        print("error: image.jpg not found next to main.py", file=sys.stderr)
        return 1
    with open(source, "rb") as fh:
        magic = fh.read(3)
    if magic != b"\xff\xd8\xff":
        print("error: image.jpg is not a JPEG", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    written = os.path.getsize(target)
    expected = os.path.getsize(source)
    if written != expected:
        print("error: wrote %d bytes, expected %d" % (written, expected),
              file=sys.stderr)
        return 1
    print("wrote", target, written, "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
