#Autor:Grégory Fernandes Ramires
#TIA:41706692
#Data:10/09/2017
#Ex:01
#Leia um número inteiro de qualquer quantidade de dígitos e apresente o algarismo da unidade, dezena e centena.


#entrada

valor = int(input('Digite um numero inteiro qualquer para ser separado em unidade, dezena e centena:'))

#processamento

cent = (valor//100)%10
dez = (valor//10)%10
uni = valor%10


#saida

print('o numero é:{}\n sua centena é:{}\n sua dezena é:{}\n sua unidade é:{}'.format(valor,cent,dez,uni))