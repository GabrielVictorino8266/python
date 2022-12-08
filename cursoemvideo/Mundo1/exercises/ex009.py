# Lei um inteiro e mostre a tabuada

mynumber = int(input('Digite um numero: '))

print('Tabuado do {}'.format(mynumber))
for number2 in range (11):
        print(mynumber, 'x', number2, '=', mynumber*number2)