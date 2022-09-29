from DataRead2 import read_data
import numpy as np
from fcmeans import FCM
from python_tsp.exact import solve_tsp_dynamic_programming
from python_tsp.distances import euclidean_distance_matrix


class TraitExactor:
    def __init__(self, tz):
        self.tz = tz
        self.tz_multiple_angle = self.multiple_angle(30)
        self.tz_mere_xy = self.mere_xy(self.tz)

        self.centers = self.fuzzy_cluster()
        self.centers_mere_xy = self.mere_xy(self.centers)
        self.permutation = self.cal_distance()[0]

        self.distance = self.cal_distance()[1]
        self.delta_angle = self.gen_angle()
        self.dis_sort = self.gen_dis_sort()
        self.weight_dis = None

    def multiple_angle(self, scale):
        multi = self.tz.copy()
        for i in range(len(multi)):
            multi[i][2] = multi[i][2] * scale
        return multi

    def mere_xy(self, vectors):
        mere = vectors.copy()
        mere = np.delete(mere, 2, axis=1)
        return mere

    def fuzzy_cluster(self, n_clusters=4):
        fcm = FCM(n_clusters=n_clusters)
        fcm.fit(self.tz_multiple_angle)
        centers = fcm.centers.copy()
        labels = fcm.predict(self.tz_multiple_angle)
        del fcm
        return centers

    def cal_distance(self):
        distance_matrix = euclidean_distance_matrix(self.centers_mere_xy)
        permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
        return permutation, distance

    def cal_angle(self, angle1, angle2):
        delta = abs(angle1 - angle2)
        delta2 = min(delta, 360 - delta)
        return delta2

    def gen_angle(self):
        angle = 0
        m = 1
        pre_centers = self.multiple_angle(scale=1/3)
        for i in range(len(self.centers)):
            if m == len(self.centers):
                angle += self.cal_angle(pre_centers[self.permutation[i]][2], pre_centers[self.permutation[0]][2])
            else:
                angle += self.cal_angle(pre_centers[self.permutation[i]][2], pre_centers[self.permutation[i+1]][2])
                m += 1
        return angle

    def cal_dis(self, dot1, dot2):
        sum = (dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2
        return np.sqrt(sum)

    def gen_dis_sort(self):
        list_dis = []
        m = 1
        for i in range(len(self.centers)):
            if m == len(self.centers):
                dot1 = self.centers_mere_xy[self.permutation[i]]
                dot2 = self.centers_mere_xy[self.permutation[0]]
                list_dis.append(self.cal_dis(dot1, dot2))
            else:
                dot1 = self.centers_mere_xy[self.permutation[i]]
                dot2 = self.centers_mere_xy[self.permutation[i+1]]
                list_dis.append(self.cal_dis(dot1, dot2))
                m += 1
        list_dis.sort()
        return np.array(list_dis)

