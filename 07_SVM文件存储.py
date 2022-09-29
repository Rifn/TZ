from DataRead2 import read_data
import pandas as pd


df = pd.read_csv("./01_traits_tz.csv")
nd = df.to_numpy()
print(nd)

list_dis_rate = []
list_ang_rate = []
for i in range(499):
    trait1 = nd[2*i][1:3]
    trait2 = nd[2*i+2][1:3]
    rate_dis = abs(trait1[0] - trait2[0]) / (trait1[0] + trait2[0]) * 2
    rate_ang = abs(trait1[1] - trait2[1]) / (trait1[1] + trait2[1]) * 2
    list_dis_rate.append(rate_dis)
    list_ang_rate.append(rate_ang)
df = pd.DataFrame()
df["dis_rate"] = list_dis_rate
df["ang_rate"] = list_ang_rate
df["label"] = [0] * len(df)
print(df)
df.to_csv("./07_svm_0.csv", index=False)




