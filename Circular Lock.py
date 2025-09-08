# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 21:38:48 2025

@author: cirze
"""

#Circular Lock
def circular_lock_moves(start, target):
    # both are strings of equal length like "1234"
    moves = 0
    for s, t in zip(start, target):
        diff = abs(int(s) - int(t))
        moves += min(diff, 10 - diff)  # because circular
    return moves

# Example
start = "1234"
target = "5678"
print("Minimum moves:", circular_lock_moves(start, target))
