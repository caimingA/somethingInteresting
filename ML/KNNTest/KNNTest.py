# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from sklearn import datasets
#
# iris = datasets.load_iris()
#
# # print(iris.keys())
# X = iris.data[:, 2:4]
# print(X.shape)
#
# y = iris.target
#
# plt.scatter(X[y == 0, 0], X[y == 0, 1], color="red", marker="*")
# plt.scatter(X[y == 1, 0], X[y == 1, 1], color="blue", marker="o")
# plt.scatter(X[y == 2, 0], X[y == 2, 1], color="pink", marker="x")
# plt.xlabel("sepal length")
# plt.ylabel("sepal width")
# plt.title("iris data")
# plt.show()

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# from sklearn import datasets

raw_data_X = [[3.393533211, 2.331273381],
              [3.110073483, 1.781539638],
              [1.343808831, 3.368360954],
              [3.582294042, 4.679179110],
              [2.280362439, 2.866990263],
              [7.423436942, 4.696522875],
              [5.745051997, 3.533989803],
              [9.172168622, 2.511101045],
              [7.792783481, 3.424088941],
               [7.939820817, 0.791637231]
             ]
raw_data_y = [1, 0, 1, 0, 0, 0, 1, 0, 1, 1]

x = np.array([8.09, 3.36])

X_train = np.array(raw_data_X)
y_train = np.array(raw_data_y)

# print(X_train[y_train == 0])
plt.scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1], color="blue")
plt.scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1], color="red")
plt.scatter(x[0], x[1], color="black")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

from math import sqrt
distance = [sqrt(np.sum((x_train -x)**2)) for x_train in X_train]
distanceTest = [sqrt(np.sum(x_train -x)**2) for x_train in X_train]

print(distance)
print(distanceTest)
test1 = sqrt((3.393533211 - 8.09)**2 + (2.331273381 - 3.36)**2)
test2 = sqrt(((3.393533211 - 8.09) + (2.331273381 - 3.36))**2)
print(test1)
print(test2)