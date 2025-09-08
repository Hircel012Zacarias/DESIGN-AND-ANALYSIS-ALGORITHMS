# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:29:46 2025

@author: cirze
"""

#min and max
def minmax(arr):
    if len(arr)==1:
      return (arr[0], arr[0])
    mid=len(arr)//2
    lmin,lmax= minmax(arr[:mid])
    rmin,rmax=minmax(arr[mid:])
    return(min(lmin,rmin),max(lmax,rmax))    

arr=[1,2,3,4]
result=minmax(arr)
print(result)