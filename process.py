# -*- coding: utf-8 -*-

# 依Unicode排序
# 去除空行
# 去重
# 備份原文件

import time
import shutil

shutil.copy("data.txt", f"data_{int(time.time())}.txt")

with open("data.txt", mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    lines = list(set(lines))
    lines.sort()
    length = len(lines)
    for i in range(length):
        if lines[length - 1 - i] == "\n":
            del lines[length - 1 - i]
        else:
            pass

with open("data.txt", mode="w", encoding="utf-8") as f_:
    f_.writelines(lines)