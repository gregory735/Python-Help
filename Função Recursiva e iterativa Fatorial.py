# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:13:49 2018

@author: Grégory
"""

#Função Fatorial Recursiva


def fat(n):
    if n == 0:
        return 1
    
    return n * fat (n-1)
    
    
print(fat(5))



#%% Fatorial Iterativa

def entrada():
    num = int(input('Digite um numero inteiro'))
    return num

def fatorial (num):
    i = 1
    fat = 1
    while i <=num:
        fat = fat * i
        i = i + 1
    return fat

fat = entrada()
print(fatorial(fat))
