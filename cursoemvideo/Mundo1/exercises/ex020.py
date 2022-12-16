# Import the module
import random

nome1 = str(input("Primeiro aluno: "))
nome2 = str(input("Segundo aluno: "))
nome3 = str(input("Terceiro aluno: "))

lista = [nome1, nome2, nome3]
random.shuffle(lista)

print("A nova ordem será: ")
print(lista)


# Descobrindo sobre o método shuffle.
# Shuffle permite embaralhar um array, como o mostra o código a seguir.
# A partir de uma lista previamente criada, ele embaralha "aleatoriamente" a ordem.

# lista =  ['Nome1', 'Nome2', 'Nome3']
# random.shuffle(lista)
# print(lista)