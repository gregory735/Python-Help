"""nome: Grégory Fernandes Ramires
Data: 31/08/2017
ex: 10"""


#entrada
p1=float(input('Digite a primeira nota: '))
p2=float(input('Digite a segunda nota: '))
p3=float(input('Digite a terceira nota: '))

#processamento
media = (p1*0.2+p2*0.3+p3*0.5)


#saida
if media >= 6:
    print('está aprovado com media: {}'.format(media))
else:
    print('reprovado com media: {}'.format(media))
