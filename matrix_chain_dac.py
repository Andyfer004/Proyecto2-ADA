# matrix_chain_dac.py

def matrix_chain_order_dac(p, i, j):
    """Divide and Conquer algorithm to compute minimal multiplication cost."""
    if i == j:
        return 0

    min_cost = float('inf')
    for k in range(i, j):
        cost = (
            matrix_chain_order_dac(p, i, k)
            + matrix_chain_order_dac(p, k + 1, j)
            + p[i - 1] * p[k] * p[j]
        )
        min_cost = min(min_cost, cost)

    return min_cost

def run_example():
    dimensions = [10, 30, 5, 60]
    n = len(dimensions) - 1
    result = matrix_chain_order_dac(dimensions, 1, n)
    print("Costo mínimo (DaC):", result)

if __name__ == "__main__":
    run_example()