#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:51:49 2018

@author: gregory735
"""
#%%
def entrada():
    num = str(input('Digite um número na base decimal: '))
    x = 0
    return num, x


def decimal(num, power):
    if len(num) == 0:
        return 0
    
    final = int(num[-1]) * (2**power)
    return final + decimal(num[:-1], power+1)


num, x = entrada()
print('A conversão do binario:',num,'para decimal é:',decimal(num,x))