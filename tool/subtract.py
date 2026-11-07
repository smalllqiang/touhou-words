# -*- coding: utf-8 -*-

# 從第一個文件中移除第二個文件中有的詞條
# 即 集合A - 集合B

import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <file_a> <file_b>", file=sys.stderr)
        sys.exit(1)

    path_a = Path(sys.argv[1])
    path_b = Path(sys.argv[2])
    for path in (path_a, path_b):
        if not path.is_file():
            print(f"Error: file not found: {path}", file=sys.stderr)
            sys.exit(1)

    with open(path_b, mode="r", encoding="utf-8") as f:
        exclude = {line.strip() for line in f}

    with open(path_a, mode="r", encoding="utf-8") as f:
        lines = [line for line in f if line.strip() not in exclude]

    with open(path_a, mode="w", encoding="utf-8") as f_:
        f_.writelines(lines)


if __name__ == "__main__":
    main()
