# Algoritmos Greedy y Programación Dinámica

## Algoritmos Greedy (Voraces)

Los algoritmos greedy son una estrategia de resolución de problemas que sigue la idea de elegir la opción óptima local en cada paso con la esperanza de encontrar el óptimo global al final. No garantizan la solución óptima en todos los casos, pero son eficientes para ciertos problemas.

Estos son también conocidos como algoritmos voraces, son una metodología de resolución de problemas que sigue un enfoque iterativo y miópico. En cada paso, el algoritmo elige la opción más prometedora o "mejor" disponible sin considerar las consecuencias futuras de esa elección. Esta "mejor" opción se selecciona según un criterio de optimización local, con la esperanza de que estas elecciones locales conducirán a una solución global óptima para el problema completo.

Características de los Algoritmos Greedy:
- Elección Greedy: En cada paso, el algoritmo hace una elección que parece ser la mejor en ese momento, basándose en un criterio de optimización local.
- Optimización Local: No revisa las decisiones tomadas previamente ni considera las futuras. Solo se enfoca en maximizar o minimizar el criterio de selección inmediato.
- No retrocede: Una vez que se toma una decisión, el algoritmo nunca retrocede para reconsiderarla, incluso si esa decisión no resulta ser la óptima.
- Eficiencia: Los algoritmos greedy tienden a ser más eficientes en términos de tiempo de ejecución comparados con otros enfoques, aunque esto puede venir a costa de no siempre encontrar la solución óptima global.

Aplicaciones de Algoritmos Greedy:
- Problema de la mochila fraccionaria
- Algoritmo de Kruskal para encontrar el árbol de expansión mínima
- Algoritmo de Dijkstra para encontrar el camino más corto

### Ejemplo: El problema del cambio
Dado un conjunto de denominaciones de monedas y un valor de cambio, el objetivo es encontrar el número mínimo de monedas necesario para hacer ese cambio.

Denominaciones: 1, 5, 10, 25
Cambio: 36 centavos

Solución Greedy:
~~~~python
def cambio_greedy(monedas, cambio):
    monedas.sort(reverse=True)  # Ordenamos las monedas de mayor a menor
    total_monedas = 0
    for moneda in monedas:
        while cambio >= moneda:
            cambio -= moneda
            total_monedas += 1
    return total_monedas

# Ejemplo de uso
monedas = [1, 5, 10, 25]
cambio = 36
print(f"Monedas necesarias: {cambio_greedy(monedas, cambio)}")
~~~~

### Ejercicio Greedy:
Dadas denominaciones de monedas [1, 3, 4] y un valor de cambio 6, utiliza el enfoque greedy para encontrar el número mínimo de monedas necesario.



## Programación Dinámica
La programación dinámica es un método para resolver problemas complejos descomponiéndolos en subproblemas más simples y almacenando los resultados de estos para no tener que recalcularlos, optimizando así el tiempo de ejecución. Es especialmente útil en problemas de optimización.

En resumen, es una técnica para resolver problemas de optimización rompiendo el problema en subproblemas más simples, resolviéndolos una vez y almacenando sus soluciones (en lo que se llama "memoización" o mediante el uso de tabulación), de manera que cuando el mismo subproblema ocurre nuevamente, la solución ya está disponible y no es necesario recalcularla.

Características de la Programación Dinámica:
- Descomposición en Subproblemas: La PD descompone el problema principal en subproblemas más pequeños y manejables.
- Almacenamiento de Soluciones: Almacena las soluciones de los subproblemas en una tabla (array o matriz), evitando así el trabajo redundante de resolver el mismo subproblema varias veces.
- Solución de Abajo hacia Arriba (Bottom-Up) o de Arriba hacia Abajo (Top-Down): Puede construir soluciones empezando desde los subproblemas más simples y subiendo hacia el problema completo (bottom-up) o descomponiendo el problema principal en subproblemas de manera recursiva hasta llegar a los casos base y luego combinar esas soluciones (top-down).
- Optimización: La PD es especialmente útil en problemas de optimización, donde se busca la solución más eficiente (máximo o mínimo) entre todas las posibles.

Aplicaciones de la Programación Dinámica:
- Problema de la mochila 0-1
- Cálculo de números de Fibonacci
- Algoritmo de Bellman-Ford para encontrar el camino más corto en grafos con pesos negativos

### Ejemplo: Fibonacci
La secuencia de Fibonacci es un clásico ejemplo donde la programación dinámica puede mejorar significativamente la eficiencia respecto a una implementación recursiva simple.

Solución con Programación Dinámica:

~~~~python
def fibonacci_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Ejemplo de uso
n = 10
print(f"Fibonacci de {n}: {fibonacci_dp(n)}")
~~~~

### Ejercicio de Programación Dinámica:

Implementa una función que utilice programación dinámica para resolver el problema de la mochila 0-1, donde se te dan pesos y valores de n ítems, junto con la capacidad de la mochila W. Debes calcular la máxima ganancia total que se puede obtener sin exceder la capacidad de la mochila.


## Diferencias Clave entre Algoritmos Greedy y Programación Dinámica
- Optimalidad: Los algoritmos greedy no siempre garantizan una solución óptima global, mientras que la programación dinámica se utiliza para asegurar la solución óptima al considerar todas las posibles configuraciones.
- Retroceso: Los algoritmos greedy no retroceden para reconsiderar sus elecciones, pero la programación dinámica puede reconsiderar decisiones previas al reconstruir la solución a partir de las soluciones almacenadas de los subproblemas.
- Aplicabilidad: Los algoritmos greedy son más adecuados para problemas donde las decisiones locales óptimas conducen a una solución global óptima. La programación dinámica es adecuada para problemas que tienen una estructura de subproblemas superpuestos y un principio de optimalidad.
