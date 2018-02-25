#Autor:Grégory
#Data: 10/09/2017
#Elabore um programa que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a
#escolha da condição de pagamento. Utilize os códigos da tabela seguinte para ler qual a condição de pagamento
#escolhida e efetuar o cálculo adequado.


#entrada
etq = float(input('Digite o preço da etiqueta do produto: '))
cdg = int(input('Digite o código de 1 a 4 para a condição de pagamento: '))


#processamento e saida
if cdg == 1:
    print('Você escolheu pagar a vista.\n O preço do procuto é de: \033[01;34m{}R$\033[m\n Você recebe um desconto de \033[01;34m10%\033[m, portanto: \033[01;34m{}R$\033[m de desconto \n o valor total é de:{}R$'.format(etq,etq*10/100,etq-(etq*10/100)))
elif cdg ==2:
    print('Você escolheu pagar a vista no cartão.\n O preço do procuto é de: \033[01;34m{}R$\033[m\n Você recebe um desconto de \033[01;34m5%\033[m, portanto: \033[01;34m{}R$\033[m de desconto \n o valor total é de:{}R$'.format(etq,etq*5/100,etq-(etq*5/100)))
elif cdg ==3:
    print('Você escolheu pagar 2x sem juros, portanto sem desconto.\n O preço do procuto é de: \033[01;34m{}R$\033[m'.format(etq))
elif cdg == 4:
    print('Você escolheu pagar 3x com juros de 10%\n O preço do procuto é de: \033[01;34m{}R$\033[m\n O juros é de: \033[01;34m{}\033[m\n O valor total do produto é de: \033[01;34m{}\033[m '.format(etq,etq*10/100,etq+(etq*10/100)))