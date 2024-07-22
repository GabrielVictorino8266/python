first_number = int(input("Informe o primeiro número inteiro: "))
second_number = int(input("Informe o segundo número inteiro: "))

comparison = "Primeiro maior" if first_number > second_number else "Segundo maior" if second_number > first_number else "Iguais."

print(f"O resultado da comparação é: {comparison}")