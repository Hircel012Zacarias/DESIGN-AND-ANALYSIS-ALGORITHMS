# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 10:46:39 2025

@author: cirze
"""

#Fractional Knapsack
wt=[30,45,50,55]
profit=[20,10,15,5]
capacity=20
gain=0
for i in range (len(wt)):
    if wt[i] <= capacity:
      gain += profit[i]
      capacity -= wt[i]
    else:
        fraction =capacity/wt[i]
        gain += profit[i] * fraction
        capacity = 0
        
print("Gain is: ",gain)