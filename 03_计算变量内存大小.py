from exact_traits import TraitExactor
from DataRead2 import read_data
import pandas as pd


tzs_tz = read_data("./数据/TZ_同指.txt")
tzs_tz200 = read_data("./数据/TZ_同指200_乱序后_Data.txt")
tzs_yz = read_data("./数据/TZ_异指.txt")


def show_memory(unit='KB', threshold=1):  # 查看变量占用内存情况
    '''
    :param unit: 显示的单位，可为`B`,`KB`,`MB`,`GB`
    :param threshold: 仅显示内存数值大于等于threshold的变量
    '''
    from sys import getsizeof
    scale = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}[unit]
    for i in list(globals().keys()):
        memory = eval("getsizeof({})".format(i)) // scale
        if memory >= threshold:
            print(i, memory)


this = TraitExactor(tzs_tz[0])


if __name__ == '__main__':
    this = TraitExactor(tzs_tz[0])
    a = [int(18)]*100000
    show_memory()

