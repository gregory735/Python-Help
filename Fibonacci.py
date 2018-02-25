n = int(input('Digite a quantidade de termos:'))

u = 1
p = 1
print(p,',',u,end=', ')
for i in range(2,n):
    n = u + p
    print(',',n,end='')
    p = u
    u = n