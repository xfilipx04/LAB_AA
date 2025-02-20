import time
import matplotlib.pyplot as plt
import sys

# Increase recursion limit if needed
sys.setrecursionlimit(3000)

# Fibonacci Implementations
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

def fibonacci_tabulation(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def fibonacci_iterative(n):
    if n == 0:
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

    if n == 0:
        return 0
    F = [[1, 1], [1, 0]]
    power(F, n - 1)
    return F[0][0]

# Measure Execution Time
def measure_time(func, n):
    start = time.time()
    result = func(n)
    end_time = time.time() - start
    print(f"{func.__name__}({n}) = {result}, Time: {end_time:.6f} sec")  # Debugging: Show results
    return end_time

# Test Series
test_values = [500,560,700,900,1200,5000,7000,10000,12000]  # Adjusted to avoid excessive recursion time

methods = {
    "Recursive": fibonacci_recursive,  # Added recursive function
    "Memoization": fibonacci_memoization,
    "Tabulation": fibonacci_tabulation,
    "Iterative": fibonacci_iterative,
    "Matrix Exponentiation": fibonacci_matrix,
}

# Collect Data
time_results = {method: [] for method in methods}
for n in test_values:
    for method, func in methods.items():
        if method == "Recursive" and n > 30:  # Limit pure recursion to avoid long execution
            time_results[method].append(None)  # Skip large values
        else:
            time_results[method].append(measure_time(func, n))

# Verify collected times
print("\nCollected Execution Times:")
for method, times in time_results.items():
    print(f"{method}: {times}")

# Plot Data
plt.figure(figsize=(10, 6))
for method, times in time_results.items():
    if method == "Recursive":
        plt.plot(test_values[:5], times[:5], marker='o', linestyle='-', label=method)  # Show only up to n=25
    else:
        plt.plot(test_values, times, marker='o', linestyle='-', label=method)

plt.xlabel("n (Fibonacci Index)")
plt.ylabel("Execution Time (seconds)")
plt.yscale("log")  # Log scale to handle growth
plt.title("Performance of Different Fibonacci Implementations")
plt.legend()
plt.grid(True)
plt.show()
