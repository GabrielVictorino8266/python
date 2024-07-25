import random

palpites :int = 0

numero_magico :int = random.randint(0, 10)

chute :int = 0

while True:
    chute = int(input("Chute um número inteiro entre 0 e 10: "))
    palpites += 1

    if chute == numero_magico:
        print("Parabens, ACERTO!!!")
        break

print(f"Você conseguiu acertar em {palpites} palpites.")