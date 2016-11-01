# -*- coding: utf-8 -*-
'''
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')    # 绘面
ax.scatter(x[1000: 4000], y[1000, 4000], z[1000: 4000], c='r')    # 绘点
'''

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-10, 10, 0.25)
Y = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.cos(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
