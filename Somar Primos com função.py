#-----=====Função Identificar Primos=====-----

def ePrimo(n):
    ndiv = 0
    cont = 1
    while cont <= n:
        resto = n % cont
        if resto == 0:
            ndiv = ndiv + 1
        cont = cont + 1

    if ndiv == 1 or ndiv == 2:
        return True
    else:
        return False

#=====------Função Somar Primos -----=====

def somar(qtd):
    cont2 = 0
    for i in range(qtd):
        y = int(input("Digite um número inteiro: "))
        if ePrimo(y) == True:
            cont2 = cont2 + y
    return cont2


qtd = int(input('Digite a quantidade de termnos para somar os primos: '))

print('A quantidade de termos que você somou foi: {} a Soma dos primos é de: {}'.format(qtd,somar(qtd)))
