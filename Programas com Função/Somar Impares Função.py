#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:00:05 2018

@author: gregory
"""
def somaImpares():
    casos = int(input())
    for i in range(casos):
        entrada = input()
        sep = entrada.split()
        v1 = int(sep[0])
        v2 = int(sep[1])
        somarP = 0
        if v1 < v2:
            for i in range(v1+1,v2):
                if i % 2 == 1:
                    somarP += i
            print(somarP)
        else:
            for i in range(v2+1,v1):
                if i % 2 == 1:
                    somarP += i
            print(somarP)
     
somaImpares()
                 
