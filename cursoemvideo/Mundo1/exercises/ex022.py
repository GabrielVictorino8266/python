# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.✔
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nomeCompleto = str(input('Qual o seu nome completo? '))

text = 'Seu nome em {} será {}'
# Print em UPPER CASE
print(text.format('Maiúsculas', nomeCompleto.upper()))
# Print em LOWER CASE
print(text.format('Minúsculas', nomeCompleto.lower()))

# Qtde de letras sem espaço
nomeCompletoemLista = nomeCompleto.split()
nomeCompletosemEspaco = ''.join(nomeCompletoemLista)
print('Seu nome sem espaço possui {} caracteres.'.format(len(nomeCompletosemEspaco)))
# Slução do vídeo:
# print('Seu nome possui {} letras.'.format(len(nomeCompleto) - nome.count(' ')))

primeiroNome = nomeCompleto.split()
print('Seu primeiro nome é {} e possui {} letras'.format(primeiroNome[0], len(primeiroNome[0])))
# Solução do vídeo:
# print(''.format(nome.find(' ')))