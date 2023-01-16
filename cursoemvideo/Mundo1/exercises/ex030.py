# Crie um programa que leia um número
#  inteiro e mostre na
#  tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número inteiro: '))
resposta = numero % 2
print('PAR' if resposta == 0 else 'ÍMPAR')