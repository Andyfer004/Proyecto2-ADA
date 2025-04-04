import random
import time
import matplotlib.pyplot as plt
from matrix_chain_dac import matrix_chain_order_dac
from matrix_chain_dp import matrix_chain_order_dp

# Función para generar múltiples cadenas de dimensiones aleatorias
def generar_cadenas(n_casos=30, min_size=3, max_size=16):
    """
    Genera una lista de casos de prueba con dimensiones aleatorias para las matrices.

    Parámetros:
    n_casos (int): Número total de casos a generar.
    min_size (int): Tamaño mínimo de la cadena (número de matrices + 1).
    max_size (int): Tamaño máximo de la cadena (número de matrices + 1).

    Retorna:
    lista: Lista de listas, cada una conteniendo dimensiones de matrices.
    """
    casos = []
    while len(casos) < n_casos:
        length = random.randint(min_size, max_size)  # Longitud aleatoria para la cadena
        dimensiones = [random.randint(5, 100) for _ in range(length)]  # Dimensiones aleatorias
        casos.append(dimensiones)
    return casos

# Función para medir y comparar los tiempos de ejecución de ambos algoritmos
def medir_tiempos(casos):
    """
    Mide los tiempos de ejecución de los algoritmos DaC y DP para cada caso generado.

    Parámetro:
    casos (lista): Lista de cadenas de dimensiones.

    Retorna:
    tuple: Listas con los tamaños (n), tiempos de DaC y tiempos de DP.
    """
    tiempos_dac = []
    tiempos_dp = []
    tamaños = []

    for dims in casos:
        n = len(dims) - 1  # Número de matrices
        tamaños.append(n)

        # Medimos el tiempo de ejecución para el algoritmo de Programación Dinámica (DP)
        start = time.time()
        matrix_chain_order_dp(dims)
        end = time.time()
        tiempos_dp.append(end - start)

        # Medimos el tiempo de Divide y Vencerás solo si n <= 10 (por eficiencia)
        if n <= 10:
            start = time.time()
            matrix_chain_order_dac(dims, 1, n)
            end = time.time()
            tiempos_dac.append(end - start)
        else:
            tiempos_dac.append(None)  # No se mide DaC para casos grandes

    return tamaños, tiempos_dac, tiempos_dp

# Función para graficar los resultados obtenidos
def graficar(tamaños, tiempos_dac, tiempos_dp):
    """
    Genera una gráfica comparando los tiempos de ejecución de ambos algoritmos.

    Parámetros:
    tamaños (lista): Lista con el número de matrices en cada caso.
    tiempos_dac (lista): Lista con los tiempos del algoritmo DaC.
    tiempos_dp (lista): Lista con los tiempos del algoritmo DP.
    """
    plt.figure(figsize=(10, 6))  # Tamaño de la figura
    plt.plot(tamaños, tiempos_dp, label="Programación Dinámica (DP)", marker='o')
    plt.plot(tamaños, [t if t is not None else None for t in tiempos_dac],
             label="Divide and Conquer (DaC)", marker='x')
    plt.xlabel("Número de matrices (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos de ejecución: DP vs DaC")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafica_tiempos.png")  # Guarda la imagen como archivo PNG
    plt.show()  # Muestra la gráfica en pantalla

# Código principal que se ejecuta al correr el script
if __name__ == "__main__":
    print("Generando casos de prueba...")
    casos = generar_cadenas()  # Genera los casos
    print("Midiendo tiempos de ejecución...")
    tamaños, tiempos_dac, tiempos_dp = medir_tiempos(casos)  # Mide los tiempos
    print("Generando gráfica...")
    graficar(tamaños, tiempos_dac, tiempos_dp)  # Muestra la comparación
    print("Listo. Revisa 'grafica_tiempos.png'")  # Mensaje final