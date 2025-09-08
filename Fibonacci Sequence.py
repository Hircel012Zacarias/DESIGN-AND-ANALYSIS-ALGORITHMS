# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:34:27 2025

@author: cirze
"""

#Fibonacci Sequence

def fibonacci_dp(n):
    if n <= 1:
        return n

    # DP table to store Fibonacci numbers
    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# Example
n = 10
print("Fibonacci number at position", n, ":", fibonacci_dp(n))

# Print sequence
print("Fibonacci sequence up to", n, ":", [fibonacci_dp(i) for i in range(n+1)])
