'''
Author: Jack Jparrow
Date: 2022-02-27 12:01:40
LastEditTime: 2022-02-27 15:25:23
LastEditors: Jack Jparrow
Description: 根据校验矩阵求码字
'''
import numpy as np
N = 10
K = 5
b = []
H = np.array([[ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [ 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [ 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
            [ 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
            [ 0, 0, 0, 1, 0, 0, 1, 0, 1, 1]])
for i in range(2**N):
    a = format(i, 'b')
    b.append("{:0>10s}".format(a))

v = np.zeros((2**N, N))
for i in range(2**N):
    v[i] = b[i]
    for j in range(N):
        v[i][j] = b[i][j] # v是0000000~1111111

w = np.zeros((1, N - K))
for o in range(2**N):
    if np.all(np.dot(v[o], H.T) % 2 == w):
        print(v[o])