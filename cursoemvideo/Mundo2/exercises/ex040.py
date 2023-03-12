# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
import statistics

primeiraNota = float(input('Digite a primeira Nota: '))
segundaNota = float(input('Digite a segunda Nota: '))

data = [primeiraNota, segundaNota]
mediaNota = statistics.mean(data)

# Media e maior que 7
if mediaNota > 7:
    print("APROVADO {:.1f}".format(mediaNota))
elif mediaNota < 7 and mediaNota > 5:
    # ENTRE 7 E 5
    print('RECUPERACAO {:.1f}'.format(mediaNota))
else:
    # MENOR QUE 5
    print('REPROVADO {:.1f}'.format(mediaNota))
    