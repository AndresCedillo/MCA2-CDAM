import numpy as np

def construir_matriz_A(puntos_3D, puntos_2D):
    A = []
    for (X, Y, Z), (x, y) in zip(puntos_3D, puntos_2D):
        A.append([X, Y, Z, 1, 0, 0, 0, 0, -x*X, -x*Y, -x*Z, -x])
        A.append([0, 0, 0, 0, X, Y, Z, 1, -y*X, -y*Y, -y*Z, -y])
    return np.array(A)

def DLT(puntos_3D, puntos_2D):
    A = construir_matriz_A(puntos_3D, puntos_2D)
    U, S, Vt = np.linalg.svd(A)
    P = Vt[-1].reshape(3, 4)
    return P

puntos_3D = [
    (0,0,0),
    (27,0,0),
    (0,5,0),
    (27,5,0),
    (0,0,5),
    (27,0,5),
    (0,5,5),
    (27,5,5)
]

puntos_2D = [
    (989,1618),
    (98,615),
    (1227,1452),
    (347,560),
    (1066,919),
    (1485,872),
    (342,697),
    (296,425)
]

P = DLT(puntos_3D, puntos_2D)

print("Matriz P:")
print(P)
