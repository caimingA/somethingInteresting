# from sklearn import tree
# from sklearn.datasets import load_wine
# from sklearn.model_selection import train_test_split
#
# wine = load_wine()
#
# # 红酒数据
# # print(wine)
#
# # print(wine.data)
# # print(wine.target)
# # print(wine.target_names)
#
# import pandas as pd
# #打印表
# print(pd.concat([pd.DataFrame(wine.data), pd.DataFrame(wine.target)], axis=1))
#
# print(wine.feature_names)
#
# Xtrain, Xtest, Ytrain, Ytest = train_test_split(wine.data, wine.target, test_size=0.3)
#
# #30%为测试集
# print(wine.data.shape)
# print(Xtest.shape)
# print(Xtrain.shape)
#
# #1.实例化
# clf = tree.DecisionTreeClassifier(criterion="entropy")
# #2.训练模型
# clf = clf.fit(Xtrain, Ytrain)
# #3.接口导出所需
# score_c = clf.score(Xtest, Ytest)
# print(score_c)

# 生成tree的图像
# import graphviz
# import pydotplus
# dot_data = tree.export_graphviz(clf
#                                 , feature_names = wine.feature_names
#                                 , class_names = ["A", "B", "C"]
#                                 , filled = True
#                                 , rounded = True
#                                 )
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_png("tree.png")
# graph.write_png("out.png")
#
#
#
#
#
# from sklearn.ensemble import forest
#
# rlf = forest.RandomForestClassifier(100
#                                     ,criterion = "entropy"
#                                     )
# rlf = rlf.fit(Xtrain, Ytrain)
#
# score_r = rlf.score(Xtest, Ytest)
#
# # print(score)
# print("tree : {}".format(score_c)
#       , "forest : {}".format(score_r)
#       )
#
#
# from sklearn.datasets import load_breast_cancer
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import GridSearchCV
# from sklearn.model_selection import cross_val_score
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
#
# cancer = load_breast_cancer()
# # data2 = cancer.data
# rfc2 = RandomForestClassifier(n_estimators=100
#                              # , random_state=0
#                              )
# score_pre = cross_val_score(rfc2, cancer.data, cancer.target, cv=10).mean()
# print(score_pre)
#
# # scoreN = []
# # for i in range(0, 200, 10):
# #     rfc2 = RandomForestClassifier(n_estimators=i+1
# #                                   ,n_jobs=-1
# #
# #                                   )
# #     score = cross_val_score(rfc2, cancer.data, cancer.target, cv=10).mean()
# #     scoreN.append(score)
# # print(max(scoreN), scoreN.index(max(scoreN))*10 + 1)
# # plt.figure(figsize=[20, 5])
# # plt.plot(range(1, 201, 10), scoreN)
# # plt.show()
#

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import numpy as np  #快速操作结构数组的工具
import matplotlib.pyplot as plt #画图工具
import pandas as pd #数据分析处理工具

attr_arr = [['slashdot', 'USA', 'yes', 18, 'None'],
            ['google', 'France', 'yes', 23, 'Premium'],
            ['digg', 'USA', 'yes', 24, 'Basic'],
            ['kiwitobes', 'France', 'yes', 23, 'Basic'],
            ['google', 'UK', 'no', 21, 'Premium'],
            ['(direct)', 'New Zealand', 'no', 12, 'None'],
            ['(direct)', 'UK', 'no', 21, 'Basic'],
            ['google', 'USA', 'no', 24, 'Premium'],
            ['slashdot', 'France', 'yes', 19, 'None'],
            ['digg', 'USA', 'no', 18, 'None'],
            ['google', 'UK', 'no', 18, 'None'],
            ['kiwitobes', 'UK', 'no', 19, 'None'],
            ['digg', 'New Zealand', 'yes', 12, 'Basic'],
            ['slashdot', 'UK', 'no', 21, 'None'],
            ['google', 'UK', 'yes', 18, 'Basic'],
            ['kiwitobes', 'France', 'yes', 19, 'Basic']]
# 生成属性数据集和结果数据集

dataMat = np.mat(attr_arr)
arrMat = dataMat[:, 0:4]
resultMat = dataMat[:, 4:5]

print(dataMat)
print(arrMat)
print(resultMat)

attr_names = ['src', 'address', 'FAQ', 'num']   #特征属性的名称
attr_pd = pd.DataFrame(data=arrMat, columns=attr_names)
print(attr_pd)
#
# #将数据集中的字符串转化为代表类别的数字。因为sklearn的决策树只识别数字
le = LabelEncoder()
for col in attr_pd.columns:                                            #为每一列序列化,就是将每种字符串转化为对应的数字。用数字代表类别
    attr_pd[col] = le.fit_transform(attr_pd[col])
print(attr_pd)

rlf = RandomForestClassifier()
rlf.fit(attr_pd, np.ravel(resultMat))
print(rlf)

#
result = rlf.predict([[1, 1, 1, 0]])    # 输入也必须是数字的。分别代表了每个数字所代表的属性的字符串值
print(result)

# train_test_split参数
# train_data：被划分的样本特征集
# train_target：被划分的样本标签
# test_size：如果是浮点数，在0-1之间，表示样本占比；如果是整数的话就是样本的数量
# random_state：是随机数的种子。
# Xtrain, Ytrain, Xtest, Ytest = train_test_split()

#选择排序
# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest)),
#     return newArr
#
# print(selectionSort([5, 3, 6, 2, 10]))
#
# #斐波那契
#
#
# def fibo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# for i in range(1, 11):
#     temp = fibo(i)
#     print(temp)

