# Autor:Grégory
# Data:10/09/2017
# Ler três valores para os lados de um triângulo, considerando os lados como: A, B e C. Verificar se os lados fornecidos
# formam realmente um triângulo. Se afirmativo, deverá ser indicado qual tipo de triângulo foi formado: isósceles,
# escaleno ou equilátero.



# entrada
a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

# processamento
if a<b+c and b<a+c and c<a+b:
    if a==b and b==c:
        print('OS lados fornecidos Equivale a um triangulo: \033[01;34mEquilatero\033[m')
    elif a==b or b==c or a==c:
        print('OS lados fornecidos Equivale a um triangulo: \033[01;34mIsosceles\033[m')
    else:
        print('OS lados fornecido Equivale a um triangulo: \033[01;34mEscaleno\033[m')
else:
    print('Os lados fornecidos \033[01;31mNão correspondem a um triangulo\033[m')
