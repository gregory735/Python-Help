def entrada():
    num = int(input("Numero: "))
    return num


def fibo(num):
    i = 1
    a = 0
    b = 1
    while i <  num:
        c = a + b
        print(c)
        a = b
        b = c
        i = i + 1
    return b
''
#programa
fib = entrada()
print(fibo(fib))
