# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:11:21 2018

@author: Grégory
"""
#%%

def entrada():
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    while valor1 < 0 or valor2 < 0:
        print('Entrada Invalida Digite novamente: ')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    return valor1, valor2

def mmc(valor1,valor2):
    a = valor1
    b = valor2
    resto = 1
    while resto != 0:
        resto = a % b
        a  = b
        b  = resto
    return  valor1 * valor2 / a

valor1, valor2 = entrada()
print('o Resultado é: {}'.format(mmc(valor1, valor2)))



