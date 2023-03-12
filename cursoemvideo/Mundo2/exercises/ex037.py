# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import time
from colorama import Fore, Style

print('Bem-vindo ao Sistema Conversor de Bases...')

numero = int(input('Digite um numero: '))

usuarioEscolha = int(input("Escolha uma base para converter:\r\n(1) BINARIO\r\n(2) OCTAL\r\n(3) HEXADECIMAL\r\n"))
# Aguarda 1.5 s
time.sleep(1.5)

# Escolheu base BINARIO
if usuarioEscolha == 1:
   print(Fore.BLUE+'O numero {} em BINARIO e: {}'.format(numero, bin(numero)[2:]))
elif usuarioEscolha == 2:
  # Eschola OCTAL
  print(Fore.RED+'O numero {} na base OCTAL e: {}'.format(numero, oct(numero)[2:]))
else:
  #  Escolha HEXADECIMAL
   print(Fore.GREEN+'O numero {} em HEXADECIMAL e: {}'.format(numero, hex(numero)[2:]))

# Saindo da Condicao
print(Style.RESET_ALL)