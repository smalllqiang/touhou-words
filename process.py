# -*- coding: utf-8 -*-

# 依Unicode排序
# 去除空行
# 去重
# 去除可能存在的前後空格
# 備份原文件

import time
import shutil

shutil.copy("data.txt", f"data_{int(time.time())}.txt")

with open("data.txt", mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    # 去除前後空格
    length = len(lines)
    for j in range(length):
        lines[j] =  lines[j].strip() + "\n"
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

with open("data.txt", mode="w", encoding="utf-8") as f_:
    f_.writelines(lines)