# Leia algo pelo teclado e mostre todas as informações sobre ele

content = input('Digite algo: ')

print('É somente texto? ', content.isalpha())
print('É somente número? ', content.isnumeric())
print('Texto e número? ', content.isalnum())
print('TUDO MAIÙSCULO? ', content.isupper())
print('tudo minúsculo? ', content.islower())
print('espaço em branco? ', content.isspace())