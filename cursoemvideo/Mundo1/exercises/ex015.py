# Exercício 15 aluguel de Carros.

# Escreva um programa que pergunte a quantidade de Km 
# percorridos por um carro alugado e a quantidade de 
# dias pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

KmRodadosCarro = float(input('Qtde de KMs rodado(s) pelo carro alugado? '))
DiasRodadosCarro = int(input('Informe por quantos dias você alugou o carro. '))

PrecoaPagar = (60 * DiasRodadosCarro) + (0.15 * KmRodadosCarro)

print('Você alugou o carro por {} dias e rodou {:.2f} Km com ele. Você irá pagar R$ {:.2f}'.format(DiasRodadosCarro, KmRodadosCarro, PrecoaPagar))
