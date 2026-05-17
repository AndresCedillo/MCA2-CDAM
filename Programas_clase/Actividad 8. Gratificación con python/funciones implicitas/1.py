import numpy as np
import matplotlib.pyplot as plt

# Definimos un rango amplio de x que cubra valores negativos y positivos
x = np.linspace(-5, 5, 2000)

# 1. Composición f o g: sqrt(-ln(x))
# Evaluamos con cuidado para manejar valores no reales o indefinidos
with np.errstate(invalid='ignore', divide='ignore'):
    fog = np.sqrt(-np.log(x.astype(complex)))
    # Nos quedamos solo con la parte real donde no sea compleja pura
    fog = np.where(np.abs(fog.imag) < 1e-5, fog.real, np.nan)

# 2. Composición g o f: ln(sqrt(-x))
with np.errstate(invalid='ignore', divide='ignore'):
    gof = np.log(np.sqrt(-x.astype(complex)))
    gof = np.where(np.abs(gof.imag) < 1e-5, gof.real, np.nan)

# 3. Producto fg: sqrt(-x) * ln(x)
with np.errstate(invalid='ignore', divide='ignore'):
    fg = np.sqrt(-x.astype(complex)) * np.log(x.astype(complex))
    fg = np.where(np.abs(fg.imag) < 1e-5, fg.real, np.nan)

# --- Graficación ---
plt.figure(figsize=(10, 6))

plt.plot(x, fog, label=r'$(f \circ g)(x) = \sqrt{-\ln x}$', color='blue', linewidth=2)
plt.plot(x, gof, label=r'$(g \circ f)(x) = \ln(\sqrt{-x})$', color='green', linewidth=2)
plt.plot(x, fg, label=r'$(fg)(x) = \sqrt{-x} \cdot \ln x$', color='red', linestyle='--', linewidth=2)

# Configuración de los ejes y formato
plt.axhline(0, color='black', linewidth=0.8, linestyle='-')
plt.axvline(0, color='black', linewidth=0.8, linestyle='-')
plt.title("Gráfica de Operaciones con Funciones (Interprepas)", fontsize=14)
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-5, 5)
plt.ylim(-2, 3)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

plt.show() 
