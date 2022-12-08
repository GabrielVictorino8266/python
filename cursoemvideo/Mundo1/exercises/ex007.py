#  Desenvolva um programa que leia duas notas e mostre uma média.

nota1 = int(input('Primeira Nota: '))
nota2 = int(input('Segunda Nota: '))

media = (nota1 + nota2) / 2
# media = nota1 + nota2 / 2

myText = 'A primeira nota é {}, a segunda é {} e a média final é {} .'

print(myText.format(nota1, nota2, media))