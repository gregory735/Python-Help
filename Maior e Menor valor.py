n = int(input('Digite um valor inteiro:'))
maior = n
menor = n
cont = 0
while n >= 1:
    if n > maior:
        maior = n
    n = int(input('Digite um valor inteiro:'))
    if n < menor and n > 0:
        menor = n
if n <= -1:
  print('o maior é:{}, o menor é {}'.format(maior,menor))
else:
    print('não foi digitado um valor valido')






