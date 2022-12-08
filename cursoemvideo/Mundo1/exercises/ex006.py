# Leia um número e mostre o seu dobro, triplo e a raiz quadrada.

n1 = int(input('Digite um número: '))
myText = 'O dobro de {} é {}, já o triplo é {} e, por último, a raiz quadrada é {} .'

print(myText.format(n1, n1*2, n1*3, n1**(1/2)))