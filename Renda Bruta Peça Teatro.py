#Autor: Grégory
#Data:13/09/2017
#Ex:04
#Faça um programa que receba o custo de um espetáculo teatral, o preço do convite desse espetáculo e a quantidade de
#ingressos vendidos. Esse programa deve calcular e mostrar:


#entrada
custo = float(input('digite o custo da peça teatral: '))
convite = float(input('Digite o preço dos convites:'))
vendas = int(input('Digite quantos ingressos vendidos:'))
#processamento
rb = convite * vendas
rl = (convite * vendas)-custo
lucro = rl*0.2

#saida
print(' O valor da renda bruta é de:{}\n O valor da renda liquida é de:{}\n O lucro em porcentagem é de:{}%'.format(rb,rl,lucro))