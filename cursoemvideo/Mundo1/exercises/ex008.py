# Leia o valor em metros e mostre a conversão para centimetros e militmetros.

meters = int(input('Digite a medida em metros: '))
myText = 'O valor em metros foi {}, sendo convertido em {} centímetros e {} milímetros.'

centimeters = meters * 100
milimeters = meters * 1000

print(myText.format(meters, centimeters, milimeters))
