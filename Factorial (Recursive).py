# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:44:44 2025

@author: cirze
"""

#Factorial (Recursive)
def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n-1)
    
n=4
res = fact(n)
print("Factorial of ",n,":",res)
