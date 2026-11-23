#!/usr/bin/env python3
"""Write the six-word story to /output/entry.txt."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "story.txt")
DEST = "/output/entry.txt"


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert 1 <= len(data) <= 60, "entry must be 1-60 chars"
    assert len(text.split()) == 6, "entry must be exactly six words"
    assert text.strip() == text, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DEST)
    os.chmod(DEST, 0o644)
    with open(DEST, "rb") as f:
        assert f.read() == data, "copy mismatch"


if __name__ == "__main__":
    main()
