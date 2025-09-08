# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:19:54 2025

@author: cirze
"""

#Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            print("Element found at index", i)
            return
    print("Element not found")    

arr = [1, 3, 5, 4, 7, 8, 9]
key = 1
linear_search(arr, key)

