#!/usr/bin/env python3

"""
fib_demo.py

Demonstrates three approaches to computing Fibonacci numbers:

By Rodrigo Canaan, with assistance ChatGPT

1. naive  -> plain recursive solution
2. memo   -> recursive solution with memoization
3. dp     -> bottom-up dynamic programming

Additionally tracks a rough "iteration count":
- Recursive versions:
    counts every function call
- Iterative DP version:
    counts every loop iteration

Usage:
    python fib_demo.py naive 35
    python fib_demo.py memo 35
    python fib_demo.py dp 35
"""

import sys
import time


# Global counter
counter = 0


# ------------------------------------------------------------
# 1. Naive recursive Fibonacci
# ------------------------------------------------------------
def fib_naive(n):
    global counter
    counter += 1

    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)


# ------------------------------------------------------------
# 2. Recursive Fibonacci with memoization
# ------------------------------------------------------------
def fib_memo(n, memo=None):
    global counter
    counter += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ------------------------------------------------------------
# 3. Bottom-up dynamic programming
# ------------------------------------------------------------
def fib_dp(n):
    global counter

    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        counter += 1
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
def main():
    global counter

    if len(sys.argv) != 3:
        print("Usage: python fib_demo.py <mode> <n>")
        print("Modes: naive, memo, dp")
        sys.exit(1)

    mode = sys.argv[1]
    n = int(sys.argv[2])

    functions = {
        "naive": fib_naive,
        "memo": fib_memo,
        "dp": fib_dp,
    }

    if mode not in functions:
        print(f"Unknown mode: {mode}")
        print("Choose from: naive, memo, dp")
        sys.exit(1)

    counter = 0
    fib_function = functions[mode]

    start = time.perf_counter()
    result = fib_function(n)
    end = time.perf_counter()

    print(f"Mode: {mode}")
    print(f"fib({n}) = {result}")
    print(
        f"Execution took {end - start:.6f} seconds "
        f"and {counter:,} iterations"
    )


if __name__ == "__main__":
    main()