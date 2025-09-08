# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:21:32 2025

@author: cirze
"""

#Selection Sort
def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index=i
        for j in range(i+1, len(arr)):
            if (arr[min_index]>arr[j]):
                min_index=j
                
                arr[i], arr[min_index]=arr[min_index],arr[i]
                return arr
                
                
arr=[4,5,3,7,8,9]
print (selection_sort(arr))