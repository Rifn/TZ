import pandas as pd
import numpy as np


class LocalGet:
    def __init__(self, tz_array):  # tz_array 是传入的指纹记录数组，n 行 3 列
        self.tz = tz_array
        self.len = len(tz_array)
        self.five_index = np.array(self.fin_five_dot(30))  # 记录数组中符合条件五个点的 index，为二维数组
        self.vectors = self.fin_vectors()

    def fin_five_dot(self, R_threshold):
        index_li = []
        for i in range(self.len):
            index = pd.DataFrame()
            li_dis = []
            li_j = []
            for j in range(self.len):
                if j == i:
                    continue
                dis = np.sqrt((self.tz[i][0]-self.tz[j][0])**2 + (self.tz[i][1]-self.tz[j][1])**2)
                if dis > R_threshold:
                    li_dis.append(dis)
                    li_j.append(j)
            index["j"] = li_j
            index["dis"] = li_dis
            index.sort_values(by="dis", axis=0, ascending=True, inplace=True)
            index.reset_index(drop=True, inplace=True)
            index_i = list(index["j"])
            index_li.append(index_i[0:5])
            del index, li_dis, li_j
        return index_li

    def fin_vectors(self):  # 计算每一个点的特征向量，含六个 ndarray 的列表
        vectors = []
        for i in range(self.len):
            vector = []
            vector.append(self.tz[i][0:2].copy())
            for j in range(5):
                vector.append(self.calcu_dis_theta(self.tz[i], self.tz[self.five_index[i][j]]))
            vector = np.array(vector)
            vectors.append(vector)
        return vectors

    @staticmethod
    def calcu_dis_theta(dot1, dot2):  # 输入两个点坐标，计算两个点的距离差、角度差
        dis = np.sqrt((dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2)
        delta_angle = abs(dot1[2] - dot2[2])
        delta_angle = min((360 - delta_angle), delta_angle)
        return np.array([dis, delta_angle])  # 返回包含距离与角度差的一维数组


class Match:
    def __init__(self, vectors1, vectors2):
        self.vectors1 = vectors1
        self.vectors2 = vectors2
        self.mn_shape = (len(vectors1), len(vectors2))
        self.mn = self.gen_mt_score()
        self.mt_score = self.match_score(self.mn)
        self.score = self.matrix_sum(self.mt_score, [], [])/(self.mn_shape[0] + self.mn_shape[1])

    def gen_mt_score(self):
        mn = np.zeros(self.mn_shape)
        for m in range(self.mn_shape[0]):
            for n in range(self.mn_shape[1]):
                score = self.dot_match(self.vectors1[m], self.vectors2[n])
                mn[m][n] = score
        return mn

    @staticmethod
    def dot_match(vector1, vector2, t_dis=20, t_angle=10):
        """
        :param vector1: 矩阵1， 列表格式，6个array，除第一个代表中心点坐标之外，其余代表五个临近点距离差和角度差
        :param vector2:
        :param t_dis: 距离阈值
        :param t_angle: 角度阈值
        :return:
        """
        z_score = 0
        have_matched_index = []
        for i in range(1, 6):
            for j in range(1, 6):
                if j in have_matched_index:
                    continue
                if abs(vector1[i][0]-vector2[j][0]) <= t_dis and abs(vector1[i][1]-vector2[j][1]) <= t_angle:
                    z_score += 1
                    have_matched_index.append(j)
        return z_score

    @staticmethod
    def matrix_sum(matrix, row_li, col_li):
        max_sum = 0
        row_haved = row_li
        col_haved = col_li
        if len(row_haved) == len(matrix) - 1:
            index_sum = int(((len(matrix) - 1) / 2 * len(matrix)))
            row_sub = 0
            for i in row_haved:
                row_sub += i
            col_sub = 0
            for j in col_haved:
                col_sub += j
            print("最后一个数", matrix[int(index_sum - row_sub)][int(index_sum - col_sub)])
            return matrix[int(index_sum - row_sub)][int(index_sum - col_sub)]

        for row in range(len(matrix)):
            if row in row_haved:
                continue
            row_haved.append(row)
            print(row)
            best_col = 0
            for col in range(len(matrix)):
                if col in col_haved:
                    continue
                col_haved_test = col_haved.copy()
                col_haved_test.append(col)
                present_value = matrix[row][col] + Match.matrix_sum(matrix, row_haved, col_haved_test)
                if present_value > max_sum:
                    best_col = col
                    max_sum = present_value
            col_haved.append(best_col)
        return max_sum

    @staticmethod
    def add_zero_row(matrix, target):
        row = np.zeros((1, matrix.shape[1]))
        for i in range(int(target - matrix.shape[0])):
            matrix = np.vstack((matrix, row))
        return matrix

    @staticmethod
    def add_zero_col(matrix, target):
        col = np.zeros((matrix.shape[0], 1))
        for i in range(int(target - matrix.shape[1])):
            matrix = np.hstack((matrix, col))
        return matrix

    def match_score(self, mn):  # 输入匹配矩阵
        mt_score = np.zeros((10, 10))
        mn = self.add_zero_row(mn, 90)
        mn = self.add_zero_col(mn, 90)
        rows = np.vsplit(mn, 10)
        for i in range(len(rows)):
            cols = np.hsplit(rows[i].copy(), 10)
            for j in range(len(cols)):
                mt_score[i][j] = self.matrix_sum(cols[j], [], [])
        return mt_score

# 局部矢量的数据用 hash 表存储，{center_dot: [], dot1: [dis, delta_angle], dot2: [..],..dot5[]}

# print(Match.matrix_sum([[1, 3], [2, 4]], [], []))