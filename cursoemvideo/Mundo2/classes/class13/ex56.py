# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
name_list = list()
age_list = list()
sex_list = list()

woman_under_20 = 0
oldest_man = str()
oldest_age = 0

average_age_group = float()

for person in range(0, 4):
    name = input("Informe seu nome completo: ").upper()
    name_list.append(name)
    age = int(input("Informe sua idade: "))
    age_list.append(age)
    sex = input("M/F: ").upper()
    sex_list.append(sex)

    average_age_group += age

    if age > oldest_age and sex == "M":
        oldest_age = age
        oldest_man = name

    if age < 20 and sex == "F":
        woman_under_20 += 1
    

print(f"Media idade grupo: {average_age_group / len(age_list)}")
print(f"Quantidade mulheres jovens menores que 20 anos é {woman_under_20}")
print(f"Nome homem mais velho: {oldest_man}")