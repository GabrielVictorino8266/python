# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from colorama import Fore, Style

anoNascimento = int(input('Insira seu ano de Nascimento: '))
anoAtual = int(input('Digite o ano atual: '))
# idadeAlistamento = 18

# Compara o ano com a idade para se Alistar.
if (anoAtual - anoNascimento) == 18:
  print(Fore.RED+'Aliste-se IMEDIATAMENTE!!!')
elif (anoAtual - anoNascimento) < 18:
# Menos de 18 anos.
  print(Fore.GREEN+'Quem nasceu em {} tem {} em 2022'.format(anoNascimento, anoAtual-anoNascimento))
  print(Fore.GREEN+'Ainda faltam {} anos para o alistemento.'.format(18 - (anoAtual-anoNascimento)))
  print(Fore.GREEN+'Seu alistamento sera em {}'.format((18 - (anoAtual-anoNascimento) + anoAtual)))
else:
  # Maior de 18 anos.
  print(Fore.YELLOW+'Quem nasceu em {} tem {} anos em 2022'.format(anoNascimento, anoAtual-anoNascimento))
  print(Fore.YELLOW+'Voce ja deveria ter se alistado ha {} anos.'.format((anoAtual - anoNascimento) - 18))
  print(Fore.YELLOW+'Seu alistamento foi em {}'.format(anoAtual - ((anoAtual - anoNascimento) - 18)))

print(Style.RESET_ALL)