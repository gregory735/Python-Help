"""
Aula 10 - EX LAB - 03
"""
n=int(input("Digite um número para usar na conta:"))
s=0
n1=n
for y in range (1,n1+1,1):
    s+=y/n
    if y != n1:
        print(y,"/",n,end =" + ")
    else:
        print(y,"/",n,end="")
    n-=1
    
print(" =",s)
        
