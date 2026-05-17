import numpy as np
import matplotlib.pyplot as plt

# Definir el dominio de x
x = np.linspace(-2, 2, 2000)  # Bastantes puntos para capturar la alta frecuencia

# Inicializar los vectores de las funciones en cero
f = np.zeros_like(x)
df = np.zeros_like(x)
d2f = np.zeros_like(x)

# Calcular las sumatorias desde k=1 hasta k=100
for k in range(1, 101):
    f += np.sin(2 * np.pi * (k**2) * x) / (4 * np.pi**2 * k**5) + (x**2) / (2 * k)
    df += np.cos(2 * np.pi * (k**2) * x) / (2 * np.pi * k**3) + x / k
    d2f += -k * np.sin(2 * np.pi * (k**2) * x) + 1 / k

# Graficar los resultados
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axs[0].plot(x, f, color='green')
axs[0].set_title('$f(x)$ - Curva Inocente y Suave')
axs[0].grid(True)

axs[1].plot(x, df, color='orange')
axs[1].set_title("$f'(x)$ - Primera Derivada con Ligeras Rugosidades")
axs[1].grid(True)

axs[2].plot(x, d2f, color='red', linewidth=0.5)
axs[2].set_title("$f''(x)$ - Segunda Derivada (Comportamiento Caótico)")
axs[2].grid(True)

plt.tight_layout()
plt.show()
