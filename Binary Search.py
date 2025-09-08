# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:29:29 2025

@author: cirze
"""

#Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [2, 3, 4, 5, 8]
target = 4
result = binary_search(arr, target)
print(result)
