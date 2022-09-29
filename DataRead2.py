import numpy as np
from 局部特征提取 import LocalGet


def read_data(path):
    tzs = []
    with open(path) as f:
        data = f.readlines()  # data 为 list 类型，内部是每一行的字符串
    for s in data:
        line = s.split(",")
        mere_dot = line[2:-1].copy()
        del line
        tz = [[mere_dot[3 * i], mere_dot[3 * i + 1], mere_dot[3 * i + 2]] for i in range(int(len(mere_dot) / 3))]
        tz = np.array(tz, dtype=np.int64)
        tzs.append(tz.copy())
    # print(tzs)
    return tzs

