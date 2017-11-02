import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
x = np.linspace(0.1,2,31)
print 'x:', x
y = np.linspace(-2,2,31)
print 'y', y
X,Y = np.meshgrid(x,y)
print 'X', X
print 'Y', Y
Z = -np.log(X) + X * X + Y * Y / 2 - 0.5
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()

