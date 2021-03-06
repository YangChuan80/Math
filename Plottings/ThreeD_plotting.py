import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

def f(x, y):
	z = x + y
	return z

x = np.linspace(-50, 250, 30)
y = np.linspace(-50, 250, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.contour3D(X, Y, Z, 200, cmap=plt.cm.jet)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('p')

plt.show()
