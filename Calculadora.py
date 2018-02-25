operacao = "1"

while operacao != "0":
    if operacao != "0":
        print('=-=-=-=-= Calculadora =-=-=-=-=-=-=')
        print("")
        print("Digite o valor um dos sinais abaixo para definir sua equação")
        print("")
        print("Soma.............+")
        print("Subtração........-")
        print("Multiplicação....*")
        print("Divisão........../")
        print("Sair.............0")

        operacao = str(input())
        valor1 = int(input('Digite o primeiro valor a ser calculado: '))
        valor2 = int(input('Digite o segundo valor a ser calculado: '))
        if operacao == ("+"):
            valor = valor1 + valor2
            print("O resultado é = {:.2f}".format(valor))
        elif operacao == "-":
            valor = valor1 - valor2
            print("O resultado é = {:.2f}".format(valor))
        elif operacao == "*":
            valor = valor1 * valor2
            print("O resultado é = {:.2f}".format(valor))
        elif operacao == "/":
            valor = valor1 / valor2
            print("O resultado é = {:.2f}".format(valor))

        #saida
    else:
        print("digite um valor correto")
