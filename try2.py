from math import sqrt
import time
from decimal import Decimal, getcontext
import sys

sys.setrecursionlimit(2000)  # Prevent memory overload due to deep recursion

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {}  # Reset memo dictionary for each call
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
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

small_series = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
big_series = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Ensuring all functions execute
def measure_time(func, n, timeout=5):
    start = time.time()
    try:
        result = func(n)
    except Exception as e:
        result = f"Error: {str(e)}"
    end = time.time()
    elapsed = end - start
    if elapsed > timeout:
        return "Timeout"
    return result, elapsed

print("\nMemoization (O(n)):")
for n in small_series + big_series:
    result, _ = measure_time(fibonacci_memoization, n)
    print(f"F({n}) = {result}")

print("\nTabulation (O(n)):")
for n in small_series + big_series:
    result, _ = measure_time(fibonacci_tabulation, n)
    print(f"F({n}) = {result}")

print("\nIterative (O(n)):")
for n in small_series + big_series:
    result, _ = measure_time(fibonacci_iterative, n)
    print(f"F({n}) = {result}")

print("\nMatrix Exponentiation (O(log n)):")
for n in small_series + big_series:
    result, _ = measure_time(fibonacci_matrix, n)
    print(f"F({n}) = {result}")

print("\nBinet's Formula (O(1)):")
for n in small_series:
    result, _ = measure_time(fibonacci_binet, n)
    print(f"F({n}) = {result}")

print("\nComparison Metric: Execution Time Analysis")
for n in small_series:
    result, t = measure_time(fibonacci_recursive, n, timeout=1)
    print(f"Recursive: T({n}) = {t:.6f} seconds | Result: {result}")

for n in small_series + big_series:
    for method, name in [(fibonacci_memoization, "Memoization"), (fibonacci_tabulation, "Tabulation"),
                          (fibonacci_iterative, "Iterative"), (fibonacci_matrix, "Matrix Exponentiation")]:
        result, t = measure_time(method, n, timeout=5)
        print(f"{name}: T({n}) = {t:.6f} seconds | Result: {result}")

for n in small_series:
    result, t = measure_time(fibonacci_binet, n, timeout=1)
    print(f"Binet's Formula: T({n}) = {t:.6f} seconds | Result: {result}")
