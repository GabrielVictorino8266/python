sum = 0

for question in range(0, 6):
    number = int(input("Informe um numero inteiro para somar: "))
    sum += number if number % 2 == 0 else int(0)

print(f"Soma final: {sum}")