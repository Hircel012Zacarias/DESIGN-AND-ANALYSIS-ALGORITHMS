# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:27:44 2025

@author: cirze
"""

#Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j=i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key

arr=[1,4,2,1,6,4,2,7,3,4]
insertion_sort(arr)
print(arr)
