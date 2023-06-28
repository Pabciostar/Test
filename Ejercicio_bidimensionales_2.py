import random
import numpy as np

llave = True
i = 0
j = 0
n = 100
arreglo_filas = []
arreglo_pxq = []
arreglo_filas_diag = []
arreglo_pxq_diag = []
fil = 3
col = 3
prom = 0
sum = 0
elem_mayor = 0
elem_menor = 100
while llave == True:
    try:
        while i < fil:
            while j < col:
                ran = random.randint(0,n)
                arreglo_filas.append(ran)
                if i == j:
                    arreglo_filas_diag.append(ran)
                else:
                    arreglo_filas_diag.append(0)
                j = j+1
                sum = sum + ran
                if elem_mayor < ran:
                    elem_mayor = ran
                elif elem_menor > ran:
                    elem_menor = ran
            arreglo_pxq.append(arreglo_filas)
            arreglo_pxq_diag.append(arreglo_filas_diag)
            arreglo_filas = []
            arreglo_filas_diag = []
            j = 0
            i = i+1
        
        print(arreglo_pxq)
        print(f"Promedio = {sum/(fil * col)}")
        print(f"Suma de los elementos = {sum}")
        print(f"El elemento mayor es = {elem_mayor}")
        print(f"El elemento menor es = {elem_menor}")
        print(arreglo_pxq_diag)
        llave = False
            
    except:            
        print("no")