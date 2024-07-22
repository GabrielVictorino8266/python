from datetime import date

birth_year = int(input("Informe seu ano de nascimento: "))
today = date.today()
age = today.year - birth_year

if age > 18:
    print(f"Passou do tempo de alistamento faz {age - 18} ano(s). Seu alistamento foi em {today.year - (age - 18)}")
if age < 18:
    print(f"Falta {18 - age} ano(s) para se alistar.")
if age == 18:
    print(f"Este é o ano de seu alistamento.")