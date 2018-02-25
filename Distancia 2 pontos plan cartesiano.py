#Autor: Grégory Fernandes Ramires
#TIA: 41706692
#Data:10/09/2017
#EX:02
#Leia as coordenadas (x,y) de dois pontos no plano cartesiano, calcule e mostre a distância entre os dois pontos.

import math

#entrada
nx1 = float(input('Digite o valor de x1:'))
nx2 = float(input('Digite o valor de x2:'))
ny1 = float(input('digite o valor de y:'))
ny2 = float(input('digite o valor de y2:'))



#processamento

dist = math.sqrt((nx2-nx1)**2+(ny2-ny1)**2)


#saida

print('a distancia entre os dois pontos no plano cartesiano é:{}'.format(dist))
