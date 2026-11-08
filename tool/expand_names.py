# -*- coding: utf-8 -*-

# 處理姓名類詞條
# 對含有間隔號的詞條, 追加分割後的各分片,
# 以及用每種間隔號替換原間隔號形成的新詞條

import re
import sys
from pathlib import Path

SEPARATORS = [" ", "　", "・", "·"]
JOINERS = ["", "　"]


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    pattern = re.compile("[" + re.escape("".join(SEPARATORS)) + "]")

    with open(path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    result = []
    for line in lines:
        entry = line.rstrip("\r\n")
        result.append(entry)
        pieces = [piece for piece in pattern.split(entry) if piece]
        if len(pieces) < 2:
            continue
        result.extend(pieces)
        if entry.isascii():
            continue
        for joiner in JOINERS:
            result.append(joiner.join(pieces))

    with open(path, mode="w", encoding="utf-8") as f_:
        for entry in result:
            f_.write(entry + "\n")


if __name__ == "__main__":
    main()
