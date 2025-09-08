# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:23:47 2025

@author: cirze
"""

#Power function using iterative method
def power(base,exponent):
    result = 1
    for i in range(exponent):
        result = base * result
    return result

base = 2
exponent = 5
res = power(base, exponent)
print(res)
