import numpy as np
import matplotlib.pyplot as plt
from K_mean import K_mean_withnumpy, plot_cluster


points = np.loadtxt('points_cluster.csv', delimiter=',', dtype=float)
bounds = {
    'x': (points[:,0].min(), points[:,0].max()),
    'y': (points[:,1].min(), points[:,1].max())
}
print(f"Bounds: X: [{bounds['x'][0]:.2f}, {bounds['x'][1]:.2f}], Y: [{bounds['y'][0]:.2f}, {bounds['y'][1]:.2f}]")

plt.scatter(points[:,0], points[:,1])
plt.plot((bounds['x'][0], bounds['x'][1]), (bounds['y'][0], bounds['y'][0]))
plt.plot((bounds['x'][0], bounds['x'][1]), (bounds['y'][1], bounds['y'][1]))
plt.plot((bounds['x'][1], bounds['x'][1]), (bounds['y'][0], bounds['y'][1]))
plt.plot((bounds['x'][0], bounds['x'][0]), (bounds['y'][0], bounds['y'][1]))
assign, finalcentroid = K_mean_withnumpy(np.array(points), 4)
for i, (cx, cy) in enumerate(finalcentroid):
    plt.scatter(cx, cy, c='black', marker='x')

plt.show()

