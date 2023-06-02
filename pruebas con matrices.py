
import numpy as np

matriz = np.array([[7,8,9],[1,2,3],[10,16,30]])
#Promedio
print(matriz.mean())
#Suma de elementos
print(matriz.sum())
#elemento mayor
print(matriz.max())
#elemento menor
print(matriz.min())
# mostrar solo la diagonal principal
print(np.diag(matriz))
#Matriz diagonal
matriz_diag =np.diag([1,2,3])
print(matriz_diag)