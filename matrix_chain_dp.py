def matrix_chain_order_dp(p):
    """
    Algoritmo de Programación Dinámica (Bottom-Up) para calcular 
    el costo mínimo de multiplicar una cadena de matrices.

    Parámetro:
    p (lista): Lista de dimensiones donde la matriz A_i tiene dimensiones p[i-1] x p[i]

    Retorna:
    int: Costo mínimo de multiplicar todas las matrices
    """
    n = len(p) - 1  # Número de matrices

    # Creamos una tabla m[i][j] donde se almacenará el costo mínimo 
    # de multiplicar matrices de A_i a A_j. Si i == j, el costo es 0.
    m = [[0 if i == j else float('inf') for j in range(n + 1)] for i in range(n + 1)]

    # length representa la longitud de la cadena de matrices que estamos evaluando
    for length in range(2, n + 1):  # Desde longitud 2 hasta n
        for i in range(1, n - length + 2):  # Índice inicial de la cadena
            j = i + length - 1  # Índice final de la cadena
            for k in range(i, j):  # k es el punto donde se parte la cadena
                # Calculamos el costo q de multiplicar A_i..A_k y A_{k+1}..A_j
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q  # Actualizamos el costo mínimo

    # El resultado final está en m[1][n], que representa el costo mínimo para A1..An
    return m[1][n]


def run_example():
    """
    Función para ejecutar un ejemplo del algoritmo.
    En este ejemplo se calcula el costo mínimo de multiplicar 
    las matrices con las dimensiones dadas.
    """
    dimensions = [10, 30, 5, 60]  # Matrices: A1 (10x30), A2 (30x5), A3 (5x60)
    result = matrix_chain_order_dp(dimensions)  # Llamamos a la función principal
    print("Costo mínimo (DP):", result)  # Imprimimos el resultado


# Punto de entrada del script si se ejecuta directamente
if __name__ == "__main__":
    run_example()