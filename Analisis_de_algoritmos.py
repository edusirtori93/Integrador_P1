#Función de los algoritmos: 



#Algoritmo 1

def factorial(x):
    resultado = 1
    for i in range (1, x + 1):
        resultado *= i
    return resultado



#Algoritmo 2   
def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n-1)
    


import time
def medir_tiempo(funcion, n):
    inicio = time.time()
    resultado = funcion(n)
    fin = time.time()
    return resultado, fin - inicio


n = 20

resultado1, tiempo1 = medir_tiempo(factorial, n)
resultado2, tiempo2 = medir_tiempo(factorial_recur, n)

print(f"Factorial interativo: Resultado={resultado1}, Tiempo={tiempo1:.8f} segundos")
print(f"Factorial recursivo: Resultado={resultado2}, Tiempo={tiempo2:.8f} segundos")