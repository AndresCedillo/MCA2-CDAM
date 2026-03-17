import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

P1 = X**4 + 2*X**2*Y**2 + Y**4
P2 = X**4 - Y**4

fig = plt.figure(figsize=(12, 5))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, P1, cmap='viridis')
ax1.set_title('$P_1(x, y) = (x^2 + y^2)^2$')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, P2, cmap='magma')
ax2.set_title('$P_2(x, y) = x^4 - y^4$')

plt.show()
