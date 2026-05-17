import numpy as np
import matplotlib.pyplot as plt

# Definimos el parámetro 'a' (determina el tamaño de la cardioide)
a = 2

# Definimos el rango de theta de 0 a 2*pi
theta = np.linspace(0, 2 * np.pi, 1000)

# Ecuación de la Cardioide en coordenadas polares
r = a * (1 + np.cos(theta))

# Obtención de las coordenadas x, y parametrizadas
x = r * np.cos(theta)
y = r * np.sin(theta)

# Graficación
plt.plot(x, y)
plt.title("Cardioide")
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.show()
