sum = 0
counter = 0

for number in range(0, 501):
    sum += number if number % 3 == 0 and not number % 2 == 0 else int()
    counter += 1 if number % 3 == 0 and not number % 2 == 0 else int()

print(f"Soma final: {sum} com {counter} valores múltiplos de 3.")