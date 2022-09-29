from DataRead2 import read_data
import numpy as np
from fcmeans import FCM
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.distances import euclidean_distance_matrix
import pandas as pd


def cal_rate(num1, num2):
    abstract = abs(num1 - num2) / num1
    return abstract


def cal_std(nd1, nd2):  # nd1 与 nd2 都是长度为 4 的一维数组
    sum_power = 0
    for n in range(4):
        sum_power += ((nd1[n] - nd2[n]) / nd1[n]) ** 2
    std = np.sqrt(sum_power) / len(nd1)
    return std


df1 = pd.read_csv("./02_traits_tz.csv")
df2 = pd.read_csv("./02_traits_needtest.csv")
trait_matrix1 = df1.to_numpy()
trait_matrix2 = df2.to_numpy()
print(trait_matrix1)


if __name__ == "__main__":
    success_nums = 0  # 记录筛选后，成功保留的次数
    for i in range(len(trait_matrix1)):  # 对指纹集1中的每条指纹的特征进行测试
        delete_list = []  # 筛选名单，记录第 j 条不满足的特征向量，对应指纹集2中的相应指纹的索引
        for j in range(len(trait_matrix2)):  # 比对指纹集2中每条指纹的特征向量
            trait1 = trait_matrix1[i]  # 第 i 条指纹的特征向量
            trait2 = trait_matrix2[j]  # 第 j 条指纹的特征向量
            """
            判别式，根据调参后的判别式，如果二者不满足，则将 j 记录入筛选名单
            """
            rate1 = cal_rate(trait1[1], trait2[1])
            rate2 = cal_rate(trait1[2], trait2[2])
            rate3 = cal_std(trait1[3:7].copy(), trait2[3:7].copy())
            if rate1 > 0.2:
                delete_list.append(j)
                continue
            else:
                if rate3 > 0.3:
                    delete_list.append(j)

        # 指纹集1中第 i 条指纹在合并后的指纹集2中本应存在的索引表达式
        """
        """
        corespond = lambda x: x + 10001 if x % 2 == 0 else x + 9999
        expect_index = corespond(i)
        delete_rate = len(delete_list) / len(trait_matrix2)
        if expect_index not in delete_list:  # 判断与该指纹匹配的另一条指纹信息是否被删除
            success_nums += 1  # 如果没有，则记录成功筛选一次
            print("对第 %d 条指纹，指纹库指纹筛选率为 %f, 过滤掉了 %f 的指纹, 且匹配指纹还在。"
                  % (i, delete_rate, delete_rate))
        else:
            print("对第 %d 条指纹，指纹库筛选率为 %f, 过滤掉了 %f 的指纹, 匹配指纹被删掉了！！！！！！"
                  % (i, delete_rate, delete_rate))
    penetrates_rate = success_nums / len(trait_matrix1)
    print("该算法下的穿透率为 %f" % penetrates_rate)



