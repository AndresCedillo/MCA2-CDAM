import numpy as np
import matplotlib.pyplot as plt

# Crear malla
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Plano 1: x + (1/2)y + (1/3)z = 1
Z1 = 3*(1 - X - 0.5*Y)

# Plano 2: (1/2)x + (1/3)y + (1/4)z = 0
Z2 = 4*(-0.5*X - (1/3)*Y)

# Plano 3: (1/3)x + (1/4)y + (1/5)z = 0
Z3 = 5*(-(1/3)*X - (1/4)*Y)

ax.plot_surface(X, Y, Z1, alpha=0.5)
ax.plot_surface(X, Y, Z2, alpha=0.5)
ax.plot_surface(X, Y, Z3, alpha=0.5)

ax.set_title("Sistema (a)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
