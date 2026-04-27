import numpy as np
import matplotlib.pyplot as plt

x = np.arange(4)

f1 = np.ones(4)
f2 = np.array([1.01, 1.02, 1.03, 1.04])
f3 = f2**2
f4 = f2**3

plt.plot(x, f1, marker='o', label='grado 0')
plt.plot(x, f2, marker='o', label='grado 1')
plt.plot(x, f3, marker='o', label='grado 2')
plt.plot(x, f4, marker='o', label='grado 3')

plt.title("Sistema (b) - tipo Vandermonde")
plt.xlabel("índice")
plt.ylabel("valor")
plt.legend()
plt.grid()

plt.show()
