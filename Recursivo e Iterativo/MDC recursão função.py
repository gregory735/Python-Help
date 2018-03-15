# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 20:25:53 2018

@author: 41706692
"""
#%%

def mdc(x,y):
    a = max(x,y)
    b = min(x,y)
    if  a % b == 0:
        return b
    else:
        return mdc(b, (a % b))
        
        
mdc(9,12)
