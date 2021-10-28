import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def J(theta, X_b, y):
    try:
        return np.sum((y - X_b.dot(theta))**2) / len(X_b)
    except:
        return float('inf')

def dJ(theta, X_b, y):
    res = np.empty(len(theta))
    res[0] = np.sum(X_b.dot(theta) - y)#np.sum()默认参数表示求所有的和，即对矩阵中所有元素求和
    for i in range(1, len(theta)):
        #(X_b.dot(theta) - y)  结果矩阵维度是 样本数*特征数 dot 特征数*1 =样本数*1   shape是（100，）表示一维数组对应的是行向量
        # .dot(X_b[:,i]) ：（100，）.dot(100,) = (1,)
        # numpy 中的一维数组可以理解成行向量
        res[i] = ((X_b.dot(theta) - y).dot(X_b[:,i]))#理解：不用np.sum()
    return res * 2 / len(X_b)


def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):
    theta = initial_theta
    cur_iter = 0

    while cur_iter < n_iters:
        gradient = dJ(theta, X_b, y)
        last_theta = theta
        theta = theta - eta * gradient
        if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
            break

        cur_iter += 1

    return theta


df = pd.read_csv("house_data.csv")
x = np.array(df["MEDV"])
y = np.array(df["RM"])
# print(x, y)

plt.scatter(x, y)
# plt.axis()
# plt.show()

X_b = np.hstack([np.ones((len(x), 1)), x.reshape(-1,1)])
initial_theta = np.zeros(X_b.shape[1])
eta = 0.01

theta = gradient_descent(X_b, y, initial_theta, eta)

print(theta)