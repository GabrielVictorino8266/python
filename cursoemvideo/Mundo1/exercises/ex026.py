# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Seu nome: '))
print("Seu nome tem silva: {}".format('SILVA' in nome.upper()))