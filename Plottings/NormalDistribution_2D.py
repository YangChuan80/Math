import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

def f(x, y):
	rho = 0.3
	a = 100
	b = 100
	sigma1 = 50
	sigma2 = 50

	i = -1/(2*(1-rho**2)) * ((x-a)**2/sigma1**2 - 2*rho*(x-a)*(y-b)/(sigma1*sigma2) + (y-b)**2/sigma2**2)

	z = math.e**i / math.pi*2*sigma1*sigma2*math.sqrt(1-rho**2)
	return z

x = np.linspace(-50, 250, 500)
y = np.linspace(-50, 250, 500)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

print(Z)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.contour3D(X, Y, Z, 200, cmap=plt.cm.jet)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('p')

plt.show()
