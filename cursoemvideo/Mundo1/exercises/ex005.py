# Leia um inteiro e mostre o antecessor e sucessor.

from cores import *

n1 = int(input('Digite um número: '))
myText = '\033[4;31;40mO número digitado é {}, seu sucessor e antecessor é, respectivamente {} e {}.\033[m'

print(myText.format(n1, n1-1, n1+1))