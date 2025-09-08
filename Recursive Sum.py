# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 21:35:15 2025

@author: cirze
"""

#Recursive Sum
def recursive_sum(n):
    # Base case
    if n == 0:
        return 0
    else:
        # Recursive step
        return n + recursive_sum(n - 1)

# Example usage
n = 5
print("Sum of first", n, "numbers:", recursive_sum(n))
