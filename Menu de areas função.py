# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#--------------- função Menu de verificação-------------
def menu ():
    print('\033[34m=-=-=-=-=-=-=-=-=-=-\033[m \033[4;31mMenu de opções\033[m \033[34m=-=-=-=-=-=-=-=-=-=-==-=\033[m')
    print("")
    print("\033[36mDigite o valor um dos sinais abaixo para selecionar sua opção\033[m")
    print("")
    print("\033[34mCalcular a Área do Quadrado....... Digite:\033[m   \033[1;31m1\033[m")
    print("\033[34mCalcular a Área do Triangulo........ Digite:\033[m   \033[1;31m2\033[m")
    print("\033[34mCalcule a Distancia de dois pontos....Digite:\033[m   \033[1;31m3\033[m")
    return
    
#-----------------------------
def quadrado():
    escolha = 1
    base = float(input('Digite a base do quadrado: '))
    altura = float(input('Digite a altura do quadrado: '))
    area = base * altura
    printar(escolha,area)
    return area
    
def triangulo():
    escolha = 2
    base = float(input('Digite a base do triangulo: '))
    altura = float(input('Digite a altura do trigulo: '))
    area = base * altura / 2
    printar(escolha,area)
    return area
    
def distanciaPontos():
    escolha = 3
    p1 = float(input('Digite o valor em metros onde o ponto 1 está: '))
    p2 = float(input('Digite o valor em metros onde o ponto 2 está: '))
    if p1 > p2:
        distancia = p1 - p2
    else:
        distancia = p2 - p1
    printar(escolha,distancia)
    return distancia

def printar(escolha,saida):
    if escolha == 1:
        print('A area do quadrado é:',saida)
    elif escolha == 2: 
        print('A area do triangulo é:',saida)
    elif escolha == 3:
        print('A distancia dos pontos é:',saida)
        
entrada = 1
while entrada != 0:
    entrada = int(input('Digite \033[31mqualquer\033[m número para abrir o menu ou Digite \033[31m0\033[m para fechar o programa:'))
    if entrada == 0:
        print('')
    else:
        menu()
        escolha = int(input('Digite sua escolha: '))
        if escolha == 1:
            quadrado()
        elif escolha == 2:
            triangulo()
        elif escolha == 3:
            distanciaPontos()