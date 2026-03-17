import matplotlib.pyplot as plt

def dibujar_chessboard_solo_puntos(centro=(2, 3)):
    x_c, y_c = centro

    plt.figure(figsize=(8, 8))
    ax = plt.gca()

    r_max = 4
    puntos_r1 = []
    puntos_r3 = []

    for xi in range(x_c - r_max, x_c + r_max + 1):
        for yi in range(y_c - r_max, y_c + r_max + 1):
            dist = max(abs(xi - x_c), abs(yi - y_c))

            color = 'lightgray'
            edge = None
            size = 50

            if dist == 1:
                color, size, edge = 'blue', 100, 'black'
                puntos_r1.append((xi, yi))
            elif dist == 3:
                color, size, edge = 'green', 100, 'black'
                puntos_r3.append((xi, yi))

            ax.scatter(xi, yi, c=color, s=size, edgecolors=edge, zorder=3)

    ax.set_title(f'Círculos Discretos bajo Métrica $d_8$ (Chessboard)\nCentro en {centro}', fontsize=12)
    ax.set_xticks(range(x_c - r_max, x_c + r_max + 1))
    ax.set_yticks(range(y_c - r_max, y_c + r_max + 1))
    ax.grid(True, linestyle=':', alpha=0.6, zorder=0)
    ax.set_aspect('equal')

    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='o', color='w', label='Radio 1', markerfacecolor='blue', markersize=10),
                       Line2D([0], [0], marker='o', color='w', label='Radio 3', markerfacecolor='green', markersize=10)]
    ax.legend(handles=legend_elements, loc='upper right')

    plt.tight_layout()
    plt.show()

    return puntos_r1, puntos_r3

r1, r3 = dibujar_chessboard_solo_puntos(centro=(2, 3))
