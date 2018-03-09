# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:17:01 2018

@author: Grégory
"""

#%% ------------------- Iterativa -----------------
def primo(n):
    ndiv = 0
    cont = 1
    while cont <= n:
        resto = n % cont
        if resto == 0:
            ndiv = ndiv + 1
        cont = cont + 1

    if ndiv == 1 or ndiv == 2:
        return True
    else:
        return False
primo(5)
#%%---------------------------Iterativo com for  ------------
def primo1(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    if count ==2:
        return True
    else:
        return False
    
primo1(11)

#%%----------------- Recursiva -------------------

def primo2(n,divisor):
    if divisor == 1:
        return True
    else:
        if n % divisor == 0:
            return False
        else:
            return primo2(n,divisor-1)


print(primo2(5,5-1)) #obs o primo2 recebe n, n-1
            
    