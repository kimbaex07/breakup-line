"""Breakup line entry for make.fun — "Dear Human: The AI Breakup Line".

Reads entry.txt next to this script, validates the competition gate
(UTF-8 text, 1-200 characters, not only whitespace), and writes the exact
bytes to $MAKEFUN_OUTPUT_DIR/entry.txt (default "output/").

Pure Python standard library only.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(here, "entry.txt")

    with open(src_path, "rb") as f:
        data = f.read()

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        print("entry.txt is not valid UTF-8", file=sys.stderr)
        return 1

    if not 1 <= len(text) <= 200:
        print(f"entry.txt must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry.txt must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry.txt must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "wb") as f:
        f.write(data)
    os.chmod(out_path, 0o644)

    print(f"wrote {out_path} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
