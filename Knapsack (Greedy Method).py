# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:38:54 2025

@author: cirze
"""

# 0/1 Knapsack (Greedy Approximation)
def Knapsack(wt, capacity, profit):
    # Calculate profit/weight ratio
    ratio = [p / w for p, w in zip(profit, wt)]
    items = sorted(zip(wt, profit, ratio), key=lambda x: x[2], reverse=True)

    gain = 0
    for w, p, r in items:
        if w <= capacity:   # now use w, not wt[i]
            gain += p
            capacity -= w
    return gain

wt = [2, 3, 1, 4, 3, 2, 7]
profit = [10, 5, 3, 2, 8, 7, 11]
capacity = 10

gain = Knapsack(wt, capacity, profit)
print("Gain:", gain)
