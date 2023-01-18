# Escreva um programa que
#  pergunte o salário de um 
# funcionário e calcule o valor do seu aumento.
#  Para salários superiores a R$1250,00, calcule 
# um aumento de 10%. Para os inferiores ou iguais, 
# o aumento é de 15%.

# Desafio da aula 10: cores no terminal 17/01/2023
from cores import *

salario = float(input('Qual o salário do funcionário? '))
if salario > 1250.00:
    aumento = salario*1.10
else:
    aumento = salario*1.15

print('{} O novo salário será R$ {:.2f} {}'.format(cores['verde'],aumento,cores['limpa']))