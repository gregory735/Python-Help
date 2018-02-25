#Autor: Grégory
#Data: 10/09/2017
#Um banco concederá um crédito especial aos seus clientes de acordo com o saldo médio no último ano. Receba o saldo
#médio de um cliente, calcule e mostre o valor do crédito, de acordo com a tabela a seguir.


#entrada
saldo = float(input('Digite o seu saldo médio do ultimo ano:'))


#processamento e saida
if saldo <= 2000.00:
    print('Seu saldo de:\033[01;34m{}\033[m Recebe um credito adicional de 10% portanto: \033[01;34m{}\033[m'.format(saldo,saldo*10/100))

elif 2000.01 <= saldo <= 3000.00:
    print('Seu saldo de:\033[01;34m{}\033[m Recebe um credito adicional de 20% portanto: \033[01;34m{}\033[m'.format(saldo,saldo*20/100))

elif 3000.01 <= saldo <= 4000.00:
    print('Seu saldo de:\033[01;34m{}\033[m Recebe um credito adicional de 25% portanto: \033[01;34m{}\033[m'.format(saldo,saldo*25/100))

elif saldo >= 4000.00:
    print('Seu saldo de:\033[01;34m{}\033[m Recebe um credito adicional de 30% portanto: \033[01;34m{}\033[m'.format(saldo,saldo*30/100))


