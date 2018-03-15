# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 19:42:49 2018

@author: Grégory
"""
#%%
def soma_rec(num):
    if(num == 0):
        return 0
    return num % 10 + soma_rec(num // 10)
    
    
soma_rec(123456789)