# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
# recebe o input do numero pelo usuario

palpite = int(input('Em que número eu pensei? '))
resposta = random.randint(0,5)
text1 = 'Eu pensei no número {} e não {}'.format(resposta, palpite)
print('Processando...')
time.sleep(2)
print('Parábens! Você venceu' if palpite == resposta else 'Ganhei! {}'.format(text1))
