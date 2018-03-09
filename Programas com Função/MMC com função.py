# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:11:21 2018

@author: Escritorio
"""
#%%

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

a = num1
b = num2

resto = 1
while resto != 0:
    resto = a % b
    a  = b
    b  = resto
    resultado = num1 * num2 / a


print(resultado)



