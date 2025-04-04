def matrix_chain_order_dac(p, i, j):
    """
    Algoritmo de Divide y Vencerás para calcular el costo mínimo 
    de multiplicar una cadena de matrices.

    Parámetros:
    p (lista): Lista de dimensiones donde la matriz A_i tiene dimensiones p[i-1] x p[i]
    i (int): Índice de inicio de la cadena (basado en 1)
    j (int): Índice de fin de la cadena (basado en 1)

    Retorna:
    int: Número mínimo de multiplicaciones escalares necesarias 
         para multiplicar las matrices de A_i a A_j
    """
    # Si solo hay una matriz, no hay multiplicación que hacer
    if i == j:
        return 0

    # Inicializamos el costo mínimo con infinito
    min_cost = float('inf')

    # Probamos todas las posiciones posibles para colocar los paréntesis
    for k in range(i, j):
        # Calculamos el costo de dividir la cadena en A_i..A_k y A_{k+1}..A_j,
        # y sumamos el costo de multiplicar los resultados intermedios
        cost = (
            matrix_chain_order_dac(p, i, k)  # Costo de multiplicar A_i hasta A_k
            + matrix_chain_order_dac(p, k + 1, j)  # Costo de multiplicar A_{k+1} hasta A_j
            + p[i - 1] * p[k] * p[j]  # Costo de multiplicar los dos resultados
        )
        # Guardamos el costo mínimo encontrado
        min_cost = min(min_cost, cost)

    # Retornamos el costo mínimo
    return min_cost


def run_example():
    """
    Función para ejecutar un ejemplo del algoritmo de matrices.
    En este ejemplo se calcula el costo mínimo de multiplicar matrices
    con dimensiones dadas en la lista 'dimensions'.
    """
    dimensions = [10, 30, 5, 60]  # Las matrices son: A1 (10x30), A2 (30x5), A3 (5x60)
    n = len(dimensions) - 1  # Número de matrices
    result = matrix_chain_order_dac(dimensions, 1, n)  # Llamada al algoritmo
    print("Costo mínimo (Divide y Vencerás):", result)  # Se muestra el resultado


# Punto de entrada del script si se ejecuta directamente
if __name__ == "__main__":
    run_example()