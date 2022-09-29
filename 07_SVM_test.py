from sklearn import svm
import pandas as pd
import numpy as np
import sklearn


df1 = pd.read_csv("./07_svm_0.csv")
df2 = pd.read_csv("./07_svm_1.csv")
nd1 = df1.to_numpy()
nd2 = df2.to_numpy()
nd = np.vstack((nd1, nd2))
print(nd, len(nd))


x, y = np.split(nd, indices_or_sections=(2,), axis=1)  # x为数据，y为标签
print(x)
print(y)

train_data, test_data, train_lable, test_label = sklearn.model_selection.train_test_split(x, y,
                                                                                          random_state=1,
                                                                                          train_size=0.6,
                                                                                          test_size=0.4)
classifier = svm.SVC(C=3, kernel="linear", gamma=10, decision_function_shape="ovr")
classifier.fit(train_data, train_lable.ravel())
# 计算分类准确率
print("训练集", classifier.score(train_data, train_lable))
print("测试集", classifier.score(test_data, test_label))

# print("决策函数", classifier.decision_function(train_data))



