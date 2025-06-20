#Función de los algoritmos: 

#Algoritmo 1
def factorial(x):
    f = 1
    for i in range (1, x + 1):
        f *= i
    return f




#Algoritmo 2   
def factorial_recur(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recur(x-1)
    
    
print(factorial(5))
print(factorial_recur(5))
 