# Análisis Comparativo de Algoritmos de Conteo en Python

## 📌 Descripción

Este proyecto tiene como objetivo comparar el rendimiento de dos algoritmos que cuentan cuántas veces aparece un número dentro de una lista en Python. El análisis incluye tanto una evaluación empírica, basada en la medición de tiempos de ejecución, como un análisis teórico, centrado en el cálculo de la complejidad algorítmica utilizando notación Big-O.

## 🧪 Algoritmos Comparados

1. **Algoritmo con bucle `for`**  
   Recorre manualmente la lista e incrementa un contador cuando se encuentra el número objetivo.

2. **Algoritmo con método `.count()`**  
   Utiliza el método nativo de las listas en Python para contar las apariciones del número.

## 🧠 Metodología

- Análisis teórico de la función T(n) de ambos algoritmos.
- Cálculo de la complejidad usando notación Big-O.
- Implementación en Python.
- Medición del tiempo de ejecución usando el módulo `time`.
- Comparación de resultados en diferentes listas de prueba.
- Documentación del análisis en formato académico.

## 📈 Resultados

- Ambos algoritmos presentan una **complejidad lineal O(n)**.
- El algoritmo con `.count()` fue **ligeramente más rápido** en pruebas empíricas, especialmente con listas más grandes.
- El algoritmo con bucle `for` es **más flexible** y permite añadir lógica condicional personalizada durante el recorrido.
