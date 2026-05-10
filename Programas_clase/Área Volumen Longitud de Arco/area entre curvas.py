import numpy as np
import matplotlib.pyplot as plt

a = 1  # Valor arbitrario para la constante a
t = np.linspace(0, 2 * np.pi, 1000)

x = a * (2 * np.cos(t) - np.cos(2 * t))
y = a * (2 * np.sin(t) - np.sin(2 * t))

plt.figure(figsize=(6,6))
plt.plot(x, y, label=f'Cardioide (a={a})', color='red')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.fill_between(x, y, alpha=0.3, color='red')
plt.title("Gráfica de la Cardioide")
plt.legend()
plt.grid(True)
plt.show()
