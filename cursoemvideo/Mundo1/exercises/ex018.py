# Crie um programa que calcule o seno, cosseno e a tangente de um ângulo informado pelo usuário.


import math
angle = float(input("Insert a value for an angle: "))

seno = math.sin(math.radians(angle))
print("O ângulo de {} graus, possui um seno de {:.2f} .".format(angle, (seno)))
cosseno = math.cos(math.radians(angle))
print("O ângulo de {} graus, possui um cosseno de {:.2f} .".format(angle, cosseno))
tangente = math.tan(math.radians(angle))
print("O ângulo de {} graus, possui uma tangente de {:.2f} .".format(angle, tangente))