# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 21:24:07 2018

@author: Grégory
"""

#função Calcular potencia



#%% --------------- Forma Iterativa ------------------
def potencia(n1,n2):

     potn = 1
     
     while n2 >= 1:
         potn *= n1
         n2 -= 1
         
     return potn
         
potencia(20,3)

#%% -------------  Forma Recursiva -----------------

def potencia2(n1,n2):
     if n2 == 0:
        return 1    
        
     return n1 * potencia2(n1,n2-1)
    
potencia(20,3)

        