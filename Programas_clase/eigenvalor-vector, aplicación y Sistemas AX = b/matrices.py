import numpy as np

def solve_eigen(name, matrix):
    print(f"--- Matriz {name} ---")
    A = np.array(matrix)

    # Calculate eigenvalores and eigenvectores
    eigenvalores, eigenvectores = np.linalg.eig(A)

    print("Eigenvalores:")
    print(eigenvalores)
    print("\nEigenvectores (columnas):")
    print(eigenvectores)
    print("-" * 30 + "\n")

# --- Case A: Hilbert-style Matrix ---
# Coefficients from:
# x + 1/2y + 1/3z
# 1/2x + 1/3y + 1/4z
# 1/3x + 1/4y + 1/5z
matrix_a = [
    [1, 1/2, 1/3],
    [1/2, 1/3, 1/4],
    [1/3, 1/4, 1/5]
]
solve_eigen("A", matrix_a)

# --- Case B: Vandermonde-style Matrix ---
# Coefficients from powers of 1.01, 1.02, 1.03, 1.04
matrix_b = [
    [1, 1, 1, 1],
    [1.01, 1.02, 1.03, 1.04],
    [1.01**2, 1.02**2, 1.03**2, 1.04**2],
    [1.01**3, 1.02**3, 1.03**3, 1.04**3]
]
solve_eigen("B", matrix_b)

# --- Case C: Ill-conditioned Matrix ---
# Coefficients from:
# x + 2y
# 2x + 4.0001y
matrix_c = [
    [1, 2],
    [2, 4.0001]
]
solve_eigen("C", matrix_c)
