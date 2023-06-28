import numpy as np
import random as rn

largo_arreglo = 10
maximo_arreglo = 100
contador_verificacion = 0


arreglo = np.arange(largo_arreglo)

for i in range(len(arreglo)):
    arreglo[i] = rn.randint(0, maximo_arreglo)
    
verificar_numero = int(input(f"Ingrese un valor entre el 0 y el {maximo_arreglo} para verificar si se encuentra en el arreglo: "))

for o in range(len(arreglo)):
    if arreglo[o] == verificar_numero:
        contador_verificacion = contador_verificacion + 1

if contador_verificacion > 0:
    print(f"el valor {verificar_numero} si se encuentra el arreglo")
elif contador_verificacion == 0:
    print(f"el valor {verificar_numero} no se encuentra el arreglo")

print(arreglo)

# Queda pendiente hacerlo con try-except, preguntar si se desea verificar otro número, elegir el largo del arreglo y el intervalo donde se moverán los números del arreglo.
