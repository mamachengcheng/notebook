# **coding: utf-8**
import numpy as np

x_1 = np.array([[5, 5], [0, 1]])
x_2 = np.array([[3, 5], [0, 1]])

m = np.asmatrix(x_1)

print(m)

print(m.T)                             # 转置

print(m.sum())                         # 各元素和

print(m.I)                             # 逆

print(m.dot(np.asmatrix(x_2)))         # 矩阵乘

print(m.min())                         # 矩阵中最小值

print(m.max())                         # 矩阵中最大值



