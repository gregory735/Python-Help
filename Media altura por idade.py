idade = 1
cont = 0
mediat = 0

while idade > 0:
    idade = int(input('Digite sua idade:'))
    if idade != 0:
      altura = float(input('Digite sua altura:'))
      if idade > 50:
        cont += 1
        mediat += altura
        mediat /= cont
if cont > 0:
 print('A media de altura é de: {}'.format(mediat))
else:
    print('não tem pessoas com mais de 50')




