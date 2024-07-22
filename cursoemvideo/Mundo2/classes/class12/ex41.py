from datetime import date

birth_year = int(input("Informe seu ano de nascimento: "))
today_year = date.today().year

age = today_year - birth_year

classifications = [
    (9, "MIRIM"),
    (14, "INFANTIL"),
    (19, "JUNIOR"),
    (25, "SÊNIOR"),
    (float("inf"), "MASTER")
]

classification = "MASTER" 
for limit, classfic in classifications:
    if age <= limit:
        classification = classfic
        break

print(f"Sua categoria é: {classification}")