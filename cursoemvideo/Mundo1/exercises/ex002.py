# Respondendo ao usuário.
# nome = input('Qual é o seu nome?')
# print('Olá, seja bem-vindo {}!'.format(nome))

# format()
# nome = 'Gabriel'
# idade = 18
# peso = 75.8

# print('{} é meu nome, já minha idade é {} anos e meu peso {} KG.'.format(nome, idade, peso))

# Format(2)

# meuTexto = "{} é o meu nome, já a minha idade é {} anos e eu peso {} KG."
# print(meuTexto.format('Gabriel', 18, 75.8))

# format() with index

from cores import *


meuTexto = "\033[33m {0} é o meu nome, já a minha idade é {1} anos e eu peso {2} KG.\033[m"
print(meuTexto.format('Gabriel', 18, 75.8))



