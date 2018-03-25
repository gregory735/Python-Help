# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 20:31:45 2018

@author: 41706692
"""
#%%
def amigos():
    lst = []
    opçao = 0
    while opçao != '8':
        print('Escolha uma opção:\n')
        print('(1) Cadastrar um amigo:')
        print('(2) Mostrar os nomes de todos os amigos:')
        print('(3) Cadastrar um amigo (no início da lista)')
        print('(4) Remover um nome')
        print('(5) Substituir um nome')
        print('(6) Mostrar o número total de amigos cadastrados')
        print('(7) Colocar os nomes dos amigos em ordem alfabética')
        print('(8) Sair do programa\n\n')
        opçao = input('Opção Selecionada: ')
        
        if opçao == '1':
            print('\n\nOpção selecionada: 1\n')
            nome = input('Digite o nome do amigo a ser cadastrado: ')
            lst.append(nome)
        elif opçao == '2': 
            print('\n\nOpção selecionada: 2\n')
            print('Amigos Cadastrados:\n')
            print('\n\n',lst,'\n')
        elif opçao == '3':
            print('\n\nOpção selecionada: 3\n')
            print('Cadastrar um amigo (no início da lista)')
            nome = input('Digite o nome do amigo a ser cadastradado no inicio da lista: ')
            lst.insert(0,nome)
            
        elif opçao == '4':
            print('\n\nOpção selecionada: 4\n')
            print('\n\n',lst,'\n')
            remover = input('Digite o nome que quer remover: ')
            lst.remove(remover)
            
        elif opçao == '5':
            print('\n\nOpção selecionada: 5\n')
            print('(5) Substituir um nome')
            nome = input('Digite o nome do amigo para ser substituido: ')
            x = int(input("Digite uma posição da lista para ser substituida: "))
            lst[x]=nome()
            
        elif opçao == '6':
            print('\n\nOpção selecionada: 6\n')
            print('(6) Mostrar o número total de amigos cadastrados')
            print(len(lst))
        elif opçao == '7':
            print('\n\nOpção selecionada: 7\n')
            print('(7) Colocar os nomes dos amigos em ordem alfabética')
            lst.sort
        else:
            print('\n\nOpção selecionada: 8\n')
            print('Saindo do programa')
            print('.')
            print('..')
            print('...')
amigos()