#Autor: Grégory
#Data:13/09/2017
#Um hotel deseja fazer uma promoção especial de final de semana, concedendo um desconto de 15% na diária. Sendo
#informados, através do teclado, o número de apartamentos do hotel e o valor da diária por apartamento para o final de
#semana completo. Elabore um programa para calcular:



#entrada
apt = int(input('Digite o número de apartamentos do hotel:'))
diaria = float(input('Digite o valor da diaria: '))

#processamento

desc = diaria*15/100
ocp100 = diaria*apt-desc
ocp70 = (diaria*apt*70/100)-desc
perda = apt*diaria - ocp100

#saida

print('O valor promocional da diaria é de: {}R$\n O valor total com a ocupação em 100% foi de: {}R%\n Com a ocupação de 70% foi de: {}R$\n O valor que o hotel perde com a promoção é de: {}R$'. format(desc,ocp100,ocp70,perda))