import numpy as np
import random as rn

fil = int(input("Ingrese el número de filas del arreglo bidimensional: "))
col = int(input("Ingrese el número de columnas del arreglo bidimensional: "))

arreglo = np.zeros([fil, col])

for i in range(fil):
    for j in range(col):
        arreglo[i][j] = rn.uniform(0.0 , 100.0)

print(arreglo)

print(f"La suma por filas se muestran a continuación:")
for n in range(fil):
    print(f"La suma de elentos de la fila {n+1} es: {arreglo[n,:].sum()}")
    

print(f"El promedio por columnas se muestran a continuación:")
for m in range(col):
    print(f"El promedio de los elementos de la columna {n+1} es: {(arreglo[:,m].sum())/col}")