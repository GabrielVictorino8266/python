# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem 
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidadeCarro = int(input('Insira a velocidade do Carro: '))
valorMulta = (velocidadeCarro - 80) * 7.00
mensagem = '{} Você ultrapassou o limite, você pagará R$ {}'.format('\033[4;31m' ,valorMulta)

print('Dentro do limite' if velocidadeCarro <= 80 else mensagem)