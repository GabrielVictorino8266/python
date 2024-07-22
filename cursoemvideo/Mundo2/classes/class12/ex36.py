home_value = float(input("Valor da casa: "))
salary = float(input("Valor do salário do comprador: "))
time_payment = int(input("Tempo para pagar (em meses): "))

installments = float(home_value / time_payment)
viability = True if installments <= salary*0.3 else False

print(f"Viability: {viability}, parcelas: R${installments:.2f}")