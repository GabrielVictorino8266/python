# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

print('Bem vindo a confederacao de Natacao.')

anoNascimento = int(input('Insera seu ano de nascimento: '))

anoNascimento = (2023 - anoNascimento)
if anoNascimento <= 9:
    # Output: MIRIM
    print('MIRIM.')
elif anoNascimento > 9 and anoNascimento <= 14:
    # Output: INFANTIL
    print('INFANTIL')
elif anoNascimento > 14 and anoNascimento <= 19:
    # Output: JUNIOR
  print('JUNIOR')
elif anoNascimento > 19 and anoNascimento <= 25:
   print('SENIOR')
else:
  #  Output: MASTER
  print('MASTER')

# condition = 'MIRIM' if anoNascimento <= 9 else 'INFANTIL' if anoNascimento <=14 else 'JUNIOR' if anoNascimento <= 19 else 'SENIOR' if anoNascimento <= 25 else 'MASTER'



# print(condition)
# print(anoNascimento)