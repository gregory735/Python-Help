#Autor: Grégory
#Data:10/09/2017
#Elabore um programa que leia notas de quatro avaliações de um aluno. A primeira avaliação tem peso 7, a segunda tem
#peso 3, a terceira peso 6 e a quarta peso 4. Calcule a média ponderada do aluno. Se a média do aluno for maior ou igual
#a 7.5, o aluno está aprovado; caso contrário, o aluno está reprovado. Mostre o resultado da decisão e a média calculada



#entrada
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
n4 = float(input('Digite a quarta nota:'))

#processamento
mf = (n1*0.7 + n2*0.3 + n3*0.6 + n4*0.4)/2

#saida
if mf >= 7.5:
    print('O aluno está \033[1;34maprovado\033[m com a média de: {}'.format(mf))
else:
    print('O aluno está \033[1;31mreprovado\033[m com a média de: {}'.format(mf))
