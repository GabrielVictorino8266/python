# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


person_name = str()
person_age = int()
person_sex = str()

average_age_group :float = 0.0

# people = [
#     {"Nome": person_name, "Idade": person_age, "Sexo": person_sex}
# ]

people = list()
oldest_age :int = 0
oldest_age_person :str = ""
woman_under_20 :int = 0

for person in range(0, 4):
    person_name = input("Informe seu nome: ").upper()
    person_age = int(input("Informe sua idade: "))
    person_sex = input("Sexo: M/F: ").upper()

    input_info = {"Nome": person_name, "Idade": person_age, "Sexo": person_sex}

    people.append(input_info)
    
    #calculates average age
    average_age_group += person_age

    #find oldest man
    if person_age > oldest_age and person_sex == "M":
        oldest_age = person_age
        oldest_age_person = person_name

    #count woman_under_20
    if person_age < 20 and person_sex == "F":
        woman_under_20 += 1


print(f"Idade media grupo: {average_age_group / len(people)}")
print(f"Nome homem mais velho: {oldest_age_person} com {oldest_age}")
print(f"Quantidade mulheres mais novas que 20 anos: {woman_under_20}.")
