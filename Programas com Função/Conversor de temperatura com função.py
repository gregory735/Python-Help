# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 00:08:58 2018
EX 03 Aula 02 LAB programação
@author: Grégory
"""
import time
#%% ----------------------- Explica o programa --------------------------------
def exibeMsg():
    print('Esse programa faz a conversão de temperatura, Fahrenheit para Celsius ou Celsius Para Fahrenheit')
    return
#%% ----------------------- Pergunta Qual opção o usuario quer ----------------
def getConvertTo():
    escolha = input('Para converter de Fahrenheit para Celsiu digite "F". Para converter de Celsius Para Fahrenheit Digite C: ')
    return escolha
#%% ----------------------- Converte fahrenheit para celsius-------------------
def exibeFahrenheitTOCelsius():
    start = float(input('Digite a temperatura em fahrenheit para ser convertida para Celsius: '))
    end = (start - 32) / 1.8
    return end
#%% ----------------------- Converte celsius para fahrenheit-------------------
def exibeCelsiusTOFahrenheit():
    start = float(input('Digite a temperatura em Celsius para ser convertida para fahrenheit : '))
    end = (start * 1.8) + 32
    return end
#%% ----------------------- Saida do programa ---------------------------------
exibeMsg()
print('\n\n')
time.sleep(1)
if getConvertTo() == 'f'.upper():
    print('Processando  .')
    time.sleep(1)
    print('Processando  ..')
    time.sleep(1)
    print('Processando  ...')
    print('Resultado é: {:.1f}'.format(exibeFahrenheitTOCelsius()))
else:
    print('Processando  .')
    time.sleep(1)
    print('Processando  ..')
    time.sleep(1)
    print('Processando  ...')
    print('Resultado é: {:.1f}'.format(exibeCelsiusTOFahrenheit()))