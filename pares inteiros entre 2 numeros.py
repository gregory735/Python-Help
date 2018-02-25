B
# coding: utf-8

# In[11]:


"""
Nome: Grégory F. Ramires TIA: 41706692
Nome: Matheus Gois TIA:41746491

EX07 Aula 01 ---- Algoritmos de programação 2 ----
"""
#entrada
valor_m = int(input('Digite o valor do "M":'))
valor_n = int(input('Digite o valor do "N":'))

#variaveis
expressao = 0
par_maximo_m = 0
par_maximo_n = 0
valor_maximo = 0

#verificação de entrada
while valor_m < 1 or valor_n < 1:
    valor_m = int(input(''))
    valor_n = int(input(''))

#processamento
for x in range (2,valor_m+1,2):
    for y in range (2,valor_n+1,2):
        expressao = x * y - x ** 2 + y
        if expressao > valor_maximo:
            valor_maximo = expressao
            par_maximo_m = x
            par_maximo_n = y
    
#saida
print('O valor máximo da expressão é: {}\nOs pares de "X" e "Y" máximo para a expressão anterior são respectivamente: {} e {}'.format(valor_maximo,valor_m,valor_n))

