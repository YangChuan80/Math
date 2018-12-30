import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

def f(x, y):
	z = x**2 - y**2
	return z

x = np.linspace(-10, 10, 30)
y = np.linspace(-10, 10, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.contour3D(X, Y, Z, 200, cmap=plt.cm.jet)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
