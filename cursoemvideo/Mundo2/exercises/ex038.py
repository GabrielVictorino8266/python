# : Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

firstNumber = int(input('Insert the first number: '))
secondNumber = int(input('Insert the second number: '))

if firstNumber > secondNumber:
    print('The first number {} is greater than second {} .'.format(firstNumber,secondNumber))
elif secondNumber > firstNumber:
    print('The second number {} is greater than first {} .'.format(secondNumber, firstNumber))
else:
    print('Both numbers {} and {} are equal.'.format(firstNumber,secondNumber))