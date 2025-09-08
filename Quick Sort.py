# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:32:59 2025

@author: cirze
"""

#Quick Sort
def Partition(arr,low,high):
    pivot=arr[high]
    pindex=low
    for j in range(low,high):
        if arr[j]<pivot:
            arr[j], arr[pindex] = arr[pindex], arr[j]
            pindex+=1
    arr[pindex], arr[high] = arr[high], arr[pindex]
    return pindex

def quick_sort(arr,low,high):
    if low<high:
        pi=Partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)
        
arr=[9,10,5,4,1,3,7]
low=1
high=10
quick_sort(arr, 0, len(arr) - 1)
print(arr)

