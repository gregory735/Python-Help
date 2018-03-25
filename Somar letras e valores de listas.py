# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%1) Escreva uma função não recursiva que receba como parâmetro uma lista de inteiros e retorne como resposta a soma de todos os elementos da lista
lst = [11,12,13,1]

def somar(soma):
    soma = sum(lst)
    return soma
    
print(somar(lst))

#%%
lst = [11,12,13,1]

def somar(soma):
    somar = 0
    for i in lst:
        somar += i
    return somar
    
    
print(somar(lst))

#%%2) Escreva uma função recursiva que receba como parâmetro uma lista de inteiros e retorne como resposta a soma de todos os elementos da lista.
lst = [11,12,13,1]
t = len(lst)-1

def recursion(lst,t):
    print(lst[t])
    if t == 0:
        return lst[0]
    return lst[t] + recursion(lst, t-1)
        
        
print(recursion(lst,t))
#%%3) Escreva uma função não recursiva que receba como parâmetros uma letra e uma palavra, e retorne quantas vezes a letra aparece dentro da palavra.
def palavrC():
    palavra = input('Digite uma palavra ou uma frase: ')
    letra = input('Digite uma letra: ')
    return palavra,letra

def contar(palavra,letra):
    cont = 0
    for i in palavra:
        if i == letra:
            cont += 1
    return cont

palavra, letra = palavrC()

print('Existem',contar(palavra,letra), 'Letras',letra, 'Na palavra/frase:',palavra)
#%%4) Escreva uma função recursiva que receba como parâmetros uma letra e uma palavra, e retorne quantas vezes a letra aparece dentro da palavra.
def palavrC():
    palavra = input('Digite uma palavra ou uma frase: ')
    letra = input('Digite uma letra: ')
    return palavra,letra

def contar(palavra,letra,t):
    if t == 0:
        return 0
    
    if palavra[t] == letra:
        return contar(palavra, letra, t-1) + 1
    else:
        return contar(palavra, letra, t-1)


palavra, letra = palavrC()
t = len(palavra)-1
print('Existem',contar(palavra,letra,t), 'Letras',letra, 'Na palavra/frase:',palavra)