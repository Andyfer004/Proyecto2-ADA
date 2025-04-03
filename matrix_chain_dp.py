# matrix_chain_dp.py

def matrix_chain_order_dp(p):
    """Bottom-Up DP algorithm to compute minimal multiplication cost."""
    n = len(p) - 1
    m = [[0 if i == j else float('inf') for j in range(n + 1)] for i in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n]

def run_example():
    dimensions = [10, 30, 5, 60]
    result = matrix_chain_order_dp(dimensions)
    print("Costo mínimo (DP):", result)

if __name__ == "__main__":
    run_example()