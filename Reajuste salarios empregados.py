reajuste = 0
salarioMasculinoMedio = 0
cont = 0
sexoFeminino = 0
nome = ""
sexoHomem = 0
numeroDeEmpregados = int(input("Digite o numero de empregados: "))

for k in range (1,numeroDeEmpregados+1):
    cont += 1
    nome = input("Digite nome: ")

    sexo = str.upper(input("Digite o sexo: "))
    while sexo != "F" and sexo != "M":
        sexo = str.upper(input("Digite Novamente seu sexo: "))

    salario = int(input("Digite seu salário: "))
    while salario < 850:
        salario = int(input("Digite novamente seu salário: "))


    if salario >= 3000:
        salario = salario+(salario*0.045)
        print ("Nome: {},teve reajuste de 4,5%, ficando com: {:.2f}.".format(nome,salario))
    if salario <= 2000:
        salario = salario + (salario * 0.085)
        print ("Nome: {},teve reajuste de 8,5%, ficando com: {:.2f}.".format(nome,salario))
    if salario < 3000 and salario >= 2000:
        salario = salario + (salario * 0.065)
        print ("Nome: {},teve reajuste de 6,5%, ficando com: {:.2f}.".format(nome,salario))
        reajuste += 1
    if sexo == "M":
        salarioMasculinoMedio += salario
        sexoHomem += 1
    if sexo == "F":
        sexoFeminino += 1
    print("---------------------------------------------------------------------------")
if cont == 0:
    print("Erro 404")
else:
    print("{} empregados receberam reajuste de 6,5%".format(reajuste))
    print("O salário médio entre homens foi de: {:.2f}".format(salarioMasculinoMedio))
    print("Percentual de empregados fenininos na empresa é: {}%".format(sexoFeminino/cont))