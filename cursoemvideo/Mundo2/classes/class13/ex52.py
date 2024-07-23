num = int(input("informe um inteiro: "))

for number in range(1, num+1):
    if num % number == 0:
        print('\033[34m', end="")
    else:
        print('\033[m', end="")
    print(f"{number}", end=" ")