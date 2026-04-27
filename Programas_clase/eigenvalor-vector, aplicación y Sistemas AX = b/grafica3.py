import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

# Ecuaciones despejadas
y1 = (3 - x) / 2
y2 = (6.0001 - 2*x) / 4.0001

plt.plot(x, y1, label="x + 2y = 3")
plt.plot(x, y2, label="2x + 4.0001y = 6.0001")

# Punto de intersección
plt.scatter(1, 1)

plt.title("Sistema (c)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

plt.show()
