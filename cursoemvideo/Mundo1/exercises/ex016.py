# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# 6.7 -> output: 6

from math import trunc
num=float(input('Digite um numero qualquer: '))

# print('O número arredondado para cima é: {}'.format(math.ceil(num)))
print('A parte inteira é: {}'.format(trunc(num)))

# Com import geral
# print('A parte inteira é: {}'.format(math.trunc(num))

# ***Sem a lib***
print('Função Interna do Python. A parte inteira é: {}'.format(int(num)))