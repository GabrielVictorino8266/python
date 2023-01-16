# If encurtado

# tempo = int(input('Quantos anos tem o seu carro? '))
# print('carro novo' if tempo<=3 else 'carro velho')
# print('--fim--')

# preco = float(input('Insira o preco de um produto: '))
# print('barato' if preco<=10.00 else 'caro')
# print('--fim--')

from argparse import MetavarTypeHelpFormatter


n1 = float(input('Insira a nota 1: '))
n2 = float(input('Insira a nota 2: '))

m = (n1 + n2) / 2
print('Suma média é {:.1f}'.format(m))
print('excelente' if m>=7 else 'repetiu de ano')