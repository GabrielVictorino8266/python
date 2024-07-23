import time
import random

menu = """
Suas ações: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA"""

while True:
    print(menu)
    user_choice = int(input("Qual é sua jogada? "))
    user_choice_text = "PEDRA" if user_choice == 0 else "PAPEL" if user_choice == 1 else "TESOURA"
    error_message = "OPCAO INVALIDA" if user_choice not in [0,1,2] else str()
    if error_message:
        print(error_message)
        break

    time.sleep(1)
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO")

    computer_choice = random.randint(0, 2)
    computer_choice_text = "PEDRA" if computer_choice == 0 else "PAPEL" if computer_choice == 1 else "TESOURA"

    print(11*"-=")
    print(f"Computador jogou {computer_choice_text}")
    print(f"Jogador jogou {user_choice_text}")
    print(11*"-=")
    winner = "EMPATE" if user_choice == computer_choice else "JOGADOR"

    if computer_choice == 0 and user_choice == 2:
        winner = "COMPUTER"
    elif computer_choice == 1 and user_choice == 0:
        winner = "COMPUTER"
    elif computer_choice == 2 and user_choice == 0:
        winner = "COMPUTER"    
    else:
        winner = winner
    print(winner)
