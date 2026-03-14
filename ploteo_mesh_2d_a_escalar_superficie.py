from matplotlib.pyplot import *
from pylab import *
from mpl_toolkits.mplot3d.axes3d import Axes3D
import numpy as np
X = np.linspace(-1, 1, 100)
Y = np.linspace(-1, 1, 100)
X,Y= np.meshgrid(X, Y)
Z=(X**3*Y**2)/(X**6+Y**4)
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2,cmap='Blues')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')

show()
