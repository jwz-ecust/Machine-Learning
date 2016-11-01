# -*- coding: utf-8 -*-
'''
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')    # 绘面
ax.scatter(x[1000: 4000], y[1000, 4000], z[1000: 4000], c='r')    # 绘点
'''

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.io as sio

# 这是存放数据点的文件,  需要它才可以画出来
mat1 = '/Users/zhangjiawei/Dropbox/Machine-Learning/code/make-love/knn/3dplot/4a.mat'
data = sio.loadmat(mat1)
m = data['data']

# 将数据分成三部分画, 在颜色上有区分度
x, y, z = m[0], m[1], m[2]
ax = plt.subplot(1, 1, 1, projection='3d')
# ax.scatter(x[:1000], y[:1000], z[:1000], c='y')
# ax.scatter(x[1000: 4000], y[1000: 4000], z[1000: 4000], c='r')
# ax.scatter(x[4000:], y[4000:], z[4000:], c='g')
ax.scatter(x, y, z)

ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()
