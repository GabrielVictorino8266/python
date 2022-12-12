# Conversor de temperaturas

# First of all, is necessary ask the user the celsius temperature
celsius = float(input('Type the celsius temperature: '))

fahrenheit = (celsius * (9/5)) + 32

print('A temperatura de {:.2f} °C corresponde a {:.2f}°F'.format(celsius, fahrenheit))