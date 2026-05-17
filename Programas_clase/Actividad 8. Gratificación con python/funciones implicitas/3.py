from sympy import symbols, plot_implicit, Eq

x, y = symbols('x y')

# --- 1. Gráfica Implícita 1 ---
eq1 = Eq(x**2 + y**3 - 2*y, 3)
p1 = plot_implicit(eq1, (x, -4, 4), (y, -3, 3),
                   title='Gráfica Implícita: $x^2 + y^3 - 2y = 3$',
                   line_color='blue', show=False)

# --- 2. Gráfica de Van der Waals ---
# Usamos x para el Volumen (V) e y para la Presión (P)
# Evitamos x <= 0.03 debido a la asíntota vertical en V = 0.03
eq2 = Eq((y + 5/(x**2)) * (x - 0.03), 9.7)
p2 = plot_implicit(eq2, (x, 0.04, 2), (y, -10, 50),
                   title="Ecuación de van der Waals (Eje X=V, Eje Y=P)",
                   line_color='purple', show=False)

# Mostrar los gráficos de forma secuencial
p1.show()
p2.show()
