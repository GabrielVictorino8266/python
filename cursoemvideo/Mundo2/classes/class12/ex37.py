print("-------------------Options-------------------")
print("|  1. Binário                               |")
print("|  2. Octal                                 |")
print("|  3. Hexadecimal                           |")
print("---------------------------------------------")

user_choice = int(input("Informe o item do menu: "))
user_number = int(input("Informe um número inteiro para conversão: "))
conversion_answer = bin(user_number) if user_choice == 1 else oct(user_number) if user_choice == 2 else hex(user_number) if user_choice == 3 else "Opção invalida, tente novamente."

print(f"Sua escolha: {user_choice}, resultado da conversão é {conversion_answer[2:]}")