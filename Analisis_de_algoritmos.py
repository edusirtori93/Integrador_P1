#Encontrar un número dentro de una lista

def contar_for(lista, numero_objetivo):
    contador = 0
    for num in lista:
        if num == numero_objetivo:
            contador += 1
    return contador
    
def contar_count(lista, numero_objetivo):
    return lista.count(numero_objetivo)

import time
def medir_tiempo(funcion, lista, numero_objetivo):
    inicio = time.time()
    resultado = funcion(lista, numero_objetivo)
    fin = time.time()
    return resultado, fin - inicio


lista1 = [1, 6, 3, 74, 2, 5, 5, 2, 9, 42, 7, 21, 6, 65, 37, 45, 5, 5, 106, 666, 787, 7, 4, 8, 23, 77, 39, 44]
lista2 = [1, 6, 3, 74, 2, 5, 5, 42,]
numero_objetivo = 5


resultado1, tiempo1 = medir_tiempo(contar_for, lista1, numero_objetivo)
resultado2, tiempo2 = medir_tiempo(contar_count, lista1, numero_objetivo)

print("Resultados con lista1:")
print(f"FOR:   {resultado1} ocurrencias en {tiempo1:.8f} segundos")
print(f"COUNT: {resultado2} ocurrencias en {tiempo2:.8f} segundos")

resultado3, tiempo3 = medir_tiempo(contar_for, lista2, numero_objetivo)
resultado4, tiempo4 = medir_tiempo(contar_count, lista2, numero_objetivo)

print("Resultados con lista2:")
print(f"FOR:   {resultado3} ocurrencias en {tiempo3:.8f} seg")
print(f"COUNT: {resultado4} ocurrencias en {tiempo4:.8f} seg")



"""
Resultados con lista1:
FOR:   4 ocurrencias en 0.00000668 segundos
COUNT: 4 ocurrencias en 0.00000525 segundos
Resultados con lista2:
FOR:   2 ocurrencias en 0.00000191 seg
COUNT: 2 ocurrencias en 0.00000191 seg
"""






