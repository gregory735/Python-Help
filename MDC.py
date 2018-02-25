n_1=int(input())
n_2=int(input())
soma=0
cont=0


#div por 2
while n_1%2==0 and n_2%2==0:
    cont+=1
    n_1=n_1/2
    n_2=n_2/2
soma+=2**cont
cont=0


#Div por 3
while n_1%3==0 and n_2%3==0:
    n_1=n_1/3
    n_2=n_2/3
    cont+=1
soma*=3**cont
cont=0


#div por 5
while n_1%5==0 and n_2%5==0:
    n_1=n_1/5
    n_2=n_2/5
    cont+=1    
soma*=5**cont
cont=0


#div por 7

while n_1%7==0 and n_2%7==0:
    n_1=n_1/7
    n_2=n_2/7
    cont+=1
soma*=7**cont
cont=0


    
    
    
print("MDC: ",soma)
