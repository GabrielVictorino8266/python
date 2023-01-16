# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
#  Km para viagens
#  de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Qual a distância da viagem? '))
print('O preço será R$ {:.2f} por {} Km.'.format(distancia*0.50, distancia) if distancia<=200 else 'O preço será R$ {:.2f} por {} Km'.format(distancia*0.45, distancia))