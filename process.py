# -*- coding: utf-8 -*-

# 依Unicode排序
# 去除空行
# 去重
# 去除可能存在的前後空格
# 備份原文件

import sys
import time
import shutil
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)

    shutil.copy(path, path.with_name(f"{path.stem}_{int(time.time())}{path.suffix}"))

    with open(path, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        # 去除前後空格
        length = len(lines)
        for j in range(length):
            lines[j] = lines[j].strip() + "\n"
        # 去重
        lines = list(set(lines))
        # 排序
        lines.sort()
        # 去除空行
        length = len(lines)
        for i in range(length):
            if lines[length - 1 - i] == "\n":
                del lines[length - 1 - i]
            else:
                pass

    with open(path, mode="w", encoding="utf-8") as f_:
        f_.writelines(lines)


if __name__ == "__main__":
    main()
