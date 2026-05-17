from sympy import symbols, cos, sin, pi
from sympy.plotting import plot_parametric

# 1. Definir el parámetro simbólico t
t = symbols('t')

# 2. Definir las ecuaciones paramétricas x(t) e y(t)
x_t = cos(t) + (1/2)*cos(7*t) + (1/3)*sin(17*t)
y_t = sin(t) + (1/2)*sin(7*t) + (1/3)*cos(17*t)

# 3. Graficar la función paramétrica en el intervalo [0, 14*pi]
# Nota: Usamos un número alto de puntos internos (adaptive_goal o nb_of_points)
# si fuera necesario, pero el graficador paramétrico adaptativo de SymPy lo maneja bien.
p = plot_parametric((x_t, y_t), (t, 0, 14*pi),
                    title="Curva Parametrizada",
                    line_color='darkcyan',
                    xlabel='x(t)', ylabel='y(t)',
                    show=False)

# 4. Mostrar el gráfico en pantalla
p.show()
