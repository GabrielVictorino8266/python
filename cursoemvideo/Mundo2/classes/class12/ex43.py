person_weight = float(input("Informe seu peso: "))
person_height = float(input("Informe sua altura: "))

imc = person_weight / person_height**2 

situation = "OBESIDADE MORBIDA"

if imc >= 30.1 and imc < 40:
    situation = "OBESIDADE"
elif imc < 30 and imc >= 25.1:
    situtation = "SOBREPESO"
elif imc <= 25 and imc >= 18.6:
    situation = "PESO IDEAL"
else:
    situation = "ABAIXO DO PESO"

print(f"Seu IMC é: {imc:.2f} e sua classficação: {situation}")