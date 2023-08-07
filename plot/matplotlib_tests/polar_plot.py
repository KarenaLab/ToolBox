
# Libraries
import numpy as np
import matplotlib.pyplot as plt


# Program
r = np.arange(start=0, stop=2, step=0.01)
theta = 2 * np.pi * r

# Plot
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

fig.suptitle("Linear plot using polar projection", fontsize=10, fontweight="bold")

ax.plot(theta, r, color="navy", linewidth=1.2, zorder=20)

ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line

ax.grid(color="lightgrey", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()


# Source
# https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html
