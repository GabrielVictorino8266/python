# Reajuste salarial

employeeSalary = float(input('Salário do empregado: '))
ammountPercentage = float(input('Porcentagem de aumento: '))
newEmployeeSalary = employeeSalary * (1 + ammountPercentage / 100)

answer = 'O novo salário será de R$ {} .'
print(answer.format(round(newEmployeeSalary, 2)))