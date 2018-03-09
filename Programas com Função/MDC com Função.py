# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 19:32:23 2018

@author: 41706692
"""
def entrada():
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    while valor1 < 0 or valor2 < 0:
        print('Entrada Invalida Digite novamente: ')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    return valor1, valor2


def MDC(valor1,valor2):  
    mdc = 1
    if valor1 > valor1:
        maior = valor2
    else:
        maior = valor2
    for i in range(1,maior):
        if valor1 % i== 0 and valor2 % i == 0:
            mdc = i
    return mdc

valor1, valor2 = entrada()
print('o Resultado é: {}'.format(MDC(valor1, valor2)))
