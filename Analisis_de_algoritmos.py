#Los siguientes algoritmos deben determinar cuantas veces aparece un número (en este caso el "5") 
# dentro de una lista.

#Algoritmo 1: bucle for
def contar_for(lista, numero_objetivo):
    contador = 0
    for num in lista:
        if num == numero_objetivo:
            contador += 1
    return contador


#Algoritmo 2: función count    
def contar_count(lista, numero_objetivo):
    return lista.count(numero_objetivo)


#Medición del tiempo de ejecución con el módulo time. 
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

print(f"Recuento del nº {numero_objetivo} en las listas.")

print("\nResultados con lista1:")
print(f"Con buble FOR: {resultado1} veces en {tiempo1:.8f} segundos")
print(f"Con función COUNT: {resultado2} veces en {tiempo2:.8f} segundos")

resultado3, tiempo3 = medir_tiempo(contar_for, lista2, numero_objetivo)
resultado4, tiempo4 = medir_tiempo(contar_count, lista2, numero_objetivo)

print("\nResultados con lista2:")
print(f"Con buble FOR: {resultado3} veces en {tiempo3:.8f} segundos")
print(f"Con función COUNT: {resultado4} veces en {tiempo4:.8f} segundos")







