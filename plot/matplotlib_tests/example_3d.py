
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data


# Data
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)

# Plot
fig = plt.figure(figsize=[8, 4.5])      # widescreen = 16:9
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
ax2 = fig.add_subplot(1, 2, 2, projection="3d")

# Plot 01 = 3D surface 
x, y = np.meshgrid(x, y)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)
surf = ax1.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax1.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=10)

# Plot 02 = 3D wireframe
x, y, z = get_test_data(0.05)
ax2.plot_wireframe(x, y, z, rstride=10, cstride=10)


plt.show()
