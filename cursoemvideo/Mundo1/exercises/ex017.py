# Crie um programa que calcule a medida da hipotenusa, sabendo os catetos oposto e adjacente.

catOp = float(input('Informe o valor do cateto Oposto: '))
catAd = float(input('Informe o valor do cateto Adjacente: '))

# from math import sqrt
# hipotenusa = sqrt(catOp*catOp + catAd*catAd)

# Usando apenas a linguagem python
# hipotenusa = (catOp** 2 + catAd**2) ** (1/2)

# Outro jeito é usando a lib math
import math
hipotenusa = math.hypot(catOp, catAd)

# print('A hipotenusa vale {}'.format(round(hipotenusa, 2)))
print('A hipotenusa vale {:.2f}'.format(hipotenusa))