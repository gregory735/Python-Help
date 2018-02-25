def calcular_mmc(num1, num2):
    mdc = num1
    y = num2

    resto = None
    while resto is not 0:
        resto = mdc % y
        mdc  = y
        y  = resto

    return (num1 * num2) / mdc


escolha = 1


while escolha != 0:
    print("")
    print("-------------Calculador de MMC-------------")
    print("1.  Iniciar cauculo MMC")
    print("0.  Sair")
    print("-------------------------------------------")

    escolha = int(input ("Favor faca sua escolha: "))

    if escolha == 1:
        num1 = int(input("Digite um numero inteiro:"))
        num2 = int(input("Digite outro numero inteiro:"))

        
        resp = calcular_mmc(num1, num2)
        print("Resultado: "+  str(resp))

    elif escolha == 0:
        print("Saindo.")
    else:
        print("Alternativa invalida")
