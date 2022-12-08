# Leia um inteiro e mostre o antecessor e sucessor.

n1 = int(input('Digite um número: '))
myText = 'O número digitado é {}, seu sucessor e antecessor é, respectivamente {} e {}.'

print(myText.format(n1, n1-1, n1+1))