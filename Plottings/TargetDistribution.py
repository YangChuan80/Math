import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

def f(x, y):
	z = 1/((1 + x**2 + y**2)**2 * math.pi)
	return z

x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.contour3D(X, Y, Z, 200, cmap=plt.cm.jet)
ax.set_xlabel('x')
ax.set_ylabel('x')
ax.set_zlabel('p')

plt.show()
