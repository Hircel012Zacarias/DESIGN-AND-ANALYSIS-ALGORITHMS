# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 09:34:21 2025

@author: cirze
"""

#Karatsuba Multiplication
def karatsuba(x,y):
    if(x<10 or y<10):
        return x*y
    
#len of the maximum number
    m=max(len(str(x)),len(str(y)))
    if(m%2!=0):
        m-=1
    #used to consume space and time, convert the values m/2 into decimal like 2.0    
    a,b=divmod(x,10**int(m/2))
    c,d=divmod(y,10**int(m/2))
    
    #recursion multiplication of ac
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    abcd=karatsuba((a+b),(c+d))-ac-bd
    return (((ac*10**m))+bd+(abcd*(10**int(m/2))))

x=int(input("Enter number 1: "))
y=int(input("Enter number 2: "))
print(karatsuba(x,y))

   
   
   
   