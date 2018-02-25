#Autor: Grégory Fernandes Ramires
#TIA: 41706692
#Data:13/09/2017
#Ex:03
#Escreva um programa que receba uma data no formato aaaammdd e a exiba no formato dd/mês/aaaa. A informação do
#mês deve ser substituído por: Janeiro, Fevereiro, ..., Dezembro.



# entrada
data = input('Digite uma data no no formato AAAAMMDD:')

# processamento
ano = data[0:4]
mes = data[4:6]
dia = data[6:8]

# saida
if mes == '01':
    print('A data é: {}/Janeiro/{}'.format(dia, ano))
elif mes == '02':
    print('A data é: {}/Fevereiro/{}'.format(dia, ano))
elif mes == '03':
    print('A data é: {}/Março/{}'.format(dia, ano))
elif mes == '04':
    print('A data é: {}/Abril/{}'.format(dia, ano))
elif mes == '05':
    print('A data é: {}/Maio/{}'.format(dia, ano))
elif mes == '06':
    print('A data é: {}/Junho/{}'.format(dia, ano))
elif mes == '07':
    print('A data é: {}/Julho/{}'.format(dia, ano))
elif mes == '08':
    print('A data é: {}/Agosto/{}'.format(dia, ano))
elif mes == '09':
    print('A data é: {}/Setembro/{}'.format(dia, ano))
elif mes == '10':
    print('A data é: {}/Outubro/{}'.format(dia, ano))
elif mes == '11':
    print('A data é: {}/Novembro/{}'.format(dia, ano))
elif mes == '12':
    print('A data é: {}/Dezembro/{}'.format(dia, ano))
