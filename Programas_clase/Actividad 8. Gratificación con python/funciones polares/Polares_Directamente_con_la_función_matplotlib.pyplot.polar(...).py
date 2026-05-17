import numpy as np
import matplotlib.pyplot as plt

# Parámetro
c = 2

# Evitar theta = 0 para no dividir entre cero
theta = np.linspace(0.1, 10, 4000)

# Función de la espiral hiperbólica
r = c / theta

# Gráfica polar
plt.figure()
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)

ax.set_title("Espiral Hiperbólica: r = c / θ")
plt.show()
