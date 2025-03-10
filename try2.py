import time
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from decimal import Decimal, getcontext

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoization(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    memo = {0: 0, 1: 1}
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]



def fibonacci_tabulation(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_matrix(n):
    def multiply_matrices(F, M):
        x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
        y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
        z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
        w = F[1][0] * M[0][1] + F[1][1] * M[1][1]
        F[0][0], F[0][1], F[1][0], F[1][1] = x, y, z, w
    
    def power(F, n):
        if n <= 1:
            return
        M = [[1, 1], [1, 0]]
        power(F, n // 2)
        multiply_matrices(F, F)
        if n % 2 != 0:
            multiply_matrices(F, M)
    
    if n <= 0:
        return 0
    F = [[1, 1], [1, 0]]
    power(F, n - 1)
    return F[0][0]

def fibonacci_binet(n):
    getcontext().prec = 100  # Increase precision
    sqrt5 = Decimal(5).sqrt()
    phi = (Decimal(1) + sqrt5) / Decimal(2)
    return round((phi**n - (-1/phi)**n) / sqrt5)

def measure_time(func, n):
    start = time.time()
    func(n)
    end = time.time()
    return end - start

# Small series for recursive function, larger for others
small_series = [5, 7, 10, 12, 15]
big_series = [50, 100, 200, 500, 1000, 2000, 5000]

methods = {
    "Recursive": fibonacci_recursive,
    "Memoization": fibonacci_memoization,
    "Tabulation": fibonacci_tabulation,
    "Iterative": fibonacci_iterative,
    "Matrix Exponentiation": fibonacci_matrix,
    "Binet's Formula": fibonacci_binet,
}

time_results = {method: [] for method in methods}

def collect_times(series, method):
    return [measure_time(methods[method], n) for n in series]

# Measure execution times
for method in methods:
    series = small_series if method == "Recursive" else big_series
    time_results[method] = collect_times(series, method)

# Plot results
plt.figure(figsize=(10, 6))
for method, times in time_results.items():
    series = small_series if method == "Recursive" else big_series
    plt.plot(series, times, marker='o', linestyle='-', label=method)

plt.xlabel("n (Fibonacci index)")
plt.ylabel("Execution Time (seconds)")
plt.title("Fibonacci Computation Time Complexity")
plt.yscale("log")  # Log scale for better visualization
plt.legend()
plt.grid()
plt.show()
