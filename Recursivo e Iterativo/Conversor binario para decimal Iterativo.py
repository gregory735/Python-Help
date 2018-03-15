#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 18:55:30 2018

@author: gregory
"""
#%%

def entrada():
    num = str(input('Digite um número na base decimal: '))
    return num

def decimal(x):
    elevando = 0
    soma = 0
    for i in x:
        soma += int(i) * 2 ** elevando
        elevando += 1
    return soma




num = entrada()
x = num[::-1]
print('A conversão do binario:',num,'para decimal é: ',decimal(x))

