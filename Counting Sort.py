# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:23:05 2025

@author: cirze
"""

#Counting sort
arr=['1','a', '4', '2','B', '1', '6','A', '4', '2', '7', '3', '4', 'a']
        
count =[0 for _ in range(128)]
for i in arr:
    count[ord(i)] += 1 
    
for i in range(len(count)):
    for j in range(count[i]):
        print(chr(i), end = ' ')
    