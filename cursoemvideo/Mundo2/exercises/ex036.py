# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
import time
from colorama import Fore, Style

print('Bem-vindo ao Sistema de Emprestimos...')

valorCasa = float(input('Informe o valor da Casa: '))
salario = float(input('Informe o valor do seu Salario: '))
quitacaoTempo = int(input('Anos para quitar: '))

print("Calculando...")
time.sleep(3)

prestacaoMensal = valorCasa / (quitacaoTempo*12)

# Compara a prestacao com a Porcentagem do Salario
if prestacaoMensal<(salario*0.3):
  print(Fore.GREEN+'Emprestimo Concedido!!!')
  print('O emprestimo sera de R$ {:.2f}'.format(prestacaoMensal))
  print(Style.RESET_ALL)
else:
    print(Fore.RED+'Emprestimo Negado!!!')
# Saindo da Condicao
print(Style.RESET_ALL)