n = int(input('Digite um valor a ser fatorado: '))
fat = 1
print(n,'! = ',end='')
for i in range(n,0,-1):
    fat *= i
    if i ==1:
      print(i,end='')
    else:
        print(i, 'x ',end='')
print(' = ',fat)
