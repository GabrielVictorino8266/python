MAX_PERSONS = 3 # qty of people
ACTUAL_YEAR = 2024

user_data = dict()
legal_age = list()
minors = list()

for user in range (1, MAX_PERSONS + 1):
    # get user information
    user_name = input("Informe seu nome: ")
    birth_year = int(input("informe seu ano de nascimento: "))
    user_data[user_name] = birth_year

    # print(user_data)

    #verify user age
    minors.append(user_name) if (ACTUAL_YEAR - user_data[user_name]) <= 18 else legal_age.append(user_name)

print(f"MENORES IDADE: {len(minors)}")
for minor in minors:
    print(minor, end=" - ")

print("ACABOU\n")

print(f"MAIOR DE IDADE: {len(legal_age)}")
for adult in legal_age:
    print(adult, end=" - ")
print("ACABOU\n")