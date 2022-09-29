import pandas as pd
import numpy as np
import pprint
import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.rcParams["font.sans-serif"] = ["SimHei"]  # 用来显示中文标签
mpl.rcParams["axes.unicode_minus"] = False  # 用来显示负号
plt.figure(figsize=(5, 5), dpi=80)


tzs_list_x = []
tzs_list_y = []
with open("./数据/TZ_同指.txt", "r") as f:
    data = f.readlines()  # data 为 list 类型，内部是每一行的字符串
for s in data:
    line = s.split(",")
    tz = line[2:-1].copy()
    tz = np.array(tz)
    x = [tz[3*i] for i in range(int(tz.size/3))]
    y = [tz[3*i+1] for i in range(int(tz.size/3))]
    x_d = np.array(x, dtype=np.int64)
    y_d = np.array(y, dtype=np.int64)
    tzs_list_x.append(x_d)
    tzs_list_y.append(y_d)

plt.scatter(tzs_list_x[3], tzs_list_y[3], label="细节点坐标")
plt.legend()
plt.savefig("./10001_1.png", dpi=500)
plt.show()

print(tzs_list_x[0], tzs_list_y[0])

print([x+y for x, y in zip(tzs_list_x[0], tzs_list_y[0])])



