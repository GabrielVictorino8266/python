# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razao: "))
counter = 0
decimo_termo = primeiro_termo + (10-1) * razao

for termo in range(primeiro_termo, decimo_termo+1, razao):
    print(termo, end=" -> ")
    counter+=1
    print(" ACABOU ") if counter == 10 else str()
