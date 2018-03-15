#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 17:43:50 2018

@author: gregory
"""
#%%

def entrada():
    num = int(input('Digite um número na base decimal: '))
    return num


def binario(num):
    if num == 0:
        return ''
    else:
        return binario(num // 2) + str(num % 2)   




num = entrada()
print('A conversão do decimal:',num,'para binário é:',binario(num))

