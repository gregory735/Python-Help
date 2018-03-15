#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:29:27 2018

@author: gregory
"""
#%%
def entrada():
    num = int(input('Digite um número na base decimal: '))
    return num

def binario(num):
    binario = ''
    while num != 0:
        
        binario += str(num % 2)
        
        num = int(num / 2)   
        
    return binario[::-1]    
   
num = entrada()
print('A conversão do decimal:',num,'para binário é: ',binario(num))
