# Faça um programa que leia um ano 
# qualquer e mostre se ele é bissexto.

import datetime

ano = int(input('Digite um ano (Digite 0 para o ano atual.): '))
if ano == 0:
    ano = datetime.date.today().year

print('O ano {} é bissexto'.format(ano) if ano % 400 == 0 and ano % 100 == 0 else 'O ano {} não é bissexto.'.format(ano))
    