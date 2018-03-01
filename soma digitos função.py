def entrada():
    num = int(input("Numero: "))
    return num

def somar (x):
    soma = 0
    while (x > 0):
        resto = x % 10
        x = (x - resto) / 10
        soma = soma + resto
    return soma

#programa
x = entrada()
print(somar(x))
