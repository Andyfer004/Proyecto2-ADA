# matrix_chain_analysis.py

import random
import time
import matplotlib.pyplot as plt
from matrix_chain_dac import matrix_chain_order_dac
from matrix_chain_dp import matrix_chain_order_dp

def generar_cadenas(n_casos=30, min_size=3, max_size=16):
    casos = []
    while len(casos) < n_casos:
        length = random.randint(min_size, max_size)
        dimensiones = [random.randint(5, 100) for _ in range(length)]
        casos.append(dimensiones)
    return casos

def medir_tiempos(casos):
    tiempos_dac = []
    tiempos_dp = []
    tamaños = []

    for dims in casos:
        n = len(dims) - 1
        tamaños.append(n)

        # Tiempo DP
        start = time.time()
        matrix_chain_order_dp(dims)
        end = time.time()
        tiempos_dp.append(end - start)

        # Tiempo DaC solo para n <= 10
        if n <= 10:
            start = time.time()
            matrix_chain_order_dac(dims, 1, n)
            end = time.time()
            tiempos_dac.append(end - start)
        else:
            tiempos_dac.append(None)

    return tamaños, tiempos_dac, tiempos_dp

def graficar(tamaños, tiempos_dac, tiempos_dp):
    plt.figure(figsize=(10, 6))
    plt.plot(tamaños, tiempos_dp, label="Programación Dinámica (DP)", marker='o')
    plt.plot(tamaños, [t if t is not None else None for t in tiempos_dac],
             label="Divide and Conquer (DaC)", marker='x')
    plt.xlabel("Número de matrices (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Comparación de tiempos de ejecución: DP vs DaC")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("grafica_tiempos.png")
    plt.show()

if __name__ == "__main__":
    print("Generando casos de prueba...")
    casos = generar_cadenas()
    print("Midiendo tiempos de ejecución...")
    tamaños, tiempos_dac, tiempos_dp = medir_tiempos(casos)
    print("Generando gráfica...")
    graficar(tamaños, tiempos_dac, tiempos_dp)
    print("Listo. Revisa 'grafica_tiempos.png'")