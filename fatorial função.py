def entrada():
    num = int(input('Digite um numero inteiro'))
    return num

def fatorial (num):
    i = 1
    fat = 1
    while i <=num:
        fat = fat * i
        i = i + 1
    return fat

fat = entrada()
print(fatorial(fat))
