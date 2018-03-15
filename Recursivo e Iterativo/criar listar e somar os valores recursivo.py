lista = []
def soma (lista,tamanho):
    if tamanho == 0:
        return lista[0]
    return lista[tamanho] + soma (lista,tamanho-1)
    
#Entrada
n = int(input("Digite um número que você queira colocar na lista:"))    
while n !=0:
    lista.append(n)
    n = int(input("Digite outro número que você queira colocar na lista (caso queria parar digite 0):"))
tamanho = len(lista)-1
print(soma(lista,tamanho))

