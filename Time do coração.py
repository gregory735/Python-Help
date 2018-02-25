ot = 0
tsp = 0
ssp = 0
pessoas = 2
tocco= 0
TocSan_Li = 0
TocSan = 0
TocCo = 0
salarioMin = float(input("Qual o valor do salário mínimo ?\n"))
nunToc = 1

while pessoas > 0:
    print("Torcedor".format(nunToc))

    timeFavorito = int(input("Pergunta 1: Qual seu time do coração?\n1-São Paulo\n2-Corinthians\n3-Santos\n4-Outros\n"))
    moradia = 0
    while timeFavorito < 0 and timeFavorito > 5:
        timeFavorito = int(input("Digite um número válido: Qual seu time do coração?\n 1-São Paulo\n2-Corinthians\n3-Santos\n4-Outros\n"))

    maradia = int(input("Pergunta 2: Onde você mora?\n1- São Paulo\n2- Litoral\n3- Interior\n"))
    while moradia < 0 and moradia > 4:
        maradia = int(input("Digite um número valido válido: Onde você mora?\n1- São Paulo\n2- Litoral\n3- Interior\n"))
    salario = float (input("Pergunta 3: Qual o seu salário?\n"))
    while salarioMin > salario:
        salario = float(input("Digite um salário válido: \n"))

    if timeFavorito == 4:
        ot += 1
    if timeFavorito == 1:
        ssp += salario
        tsp += 1
    if moradia == 1 and timeFavorito == 2:
        tocco += 1
        TocCo += 1
    if timeFavorito == 3 and moradia == 2:
        TocSan_Li += 1
        TocSan += 1
    pessoas -= 1

    nunToc += 1
print(""
      "Escolha a opção para ver a estatística\n"
      "1. Número de torcedores por clube"
      "\n2. Média salarial dos torcedores do São Paulo"
      "\n3. Número de pessoas moradoras de São Paulo, torcedoras do Corinthians"
      "\n4. Número de pessoas do Litoral torcedoras do Santos"
      "\n5. Sair.\n")
cont2 = 0
escolha = int(input("Digite uma Oção: "))
while escolha < 0 and escolha > 5:
    escolha = int(input("Digite uma Oção válida: "))

while escolha != 5:
    if escolha == 1:
        print ("são paulo tem {} torcedores".format(tsp))
        print("O Corinthians tem {} torcedores".format(TocCo))
        print ("O santos tem {} torcedores".format(TocSan))
        print ("Outros times tem {} torcedores".format(ot))
    if escolha == 2:
        mediaSp = ssp/tsp
        print ("A Média salarial dos torcedores do São Paulo é : {:.2f}".format(mediaSp))
    if escolha == 3:
        print("O número de pessoas moradoras de São Paulo, torcedoras do Corinthians é{}".format(tocco))
    if escolha == 4:
        print("O número de pessoas do Litoral torcedoras do Santos é:".format(TocSan_Li))

    escolha = int(input("Digite uma Oção: "))
    while escolha < 0 and escolha > 5:
        escolha = int(input("Digite uma Oção válida: "))