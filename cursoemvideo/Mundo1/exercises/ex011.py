# 12/11/2022

# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcula a área e a quantidade de tinta necessária 
# para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

# Code

# Firt, we receive an input from user, which represents the width and height
width = float(input('Insira a largura da parede. '))
height = float(input('Insria a altura da parede. '))

# After receive some inputs, we need make calculations, so now, we'll calculate area how much of paint is necessary.

# To calculate the area, we multiply width by height
wallArea = width * height
# now, we need to know how much of paint is necessary.
litersPaint = wallArea / 2

# Now, we show to the user the answer
response = 'A área da parede é {} m², sendo necessário {} litro(s) de tinta para pintá-la por completo.'
print(response.format(wallArea, litersPaint))
