"""
    Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso
"""

def sum(first_number :int, second_number :int):
    return first_number + second_number
    

def times(first_number :int, second_number :int):
    return first_number * second_number

def bigger(first_number :int, second_number: int):
    if first_number > second_number:
        return "Primeiro é maior."
    
    if second_number > first_number:
        return "Segundo é maior."
    
    return "Ambos são iguais."

def newNumbers(new_first_number :int, new_second_number: int):
    first_number = new_first_number
    second_number = new_second_number
    return f"Novos números são {first_number} e {second_number}" 
    
menu = """
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
"""

first_number :int = 0
second_number :int = 0

option_selected :int = 0
first_number = int(input("Primeiro valor: "))
second_number = int(input("Segundo valor: "))

while True:


    print(menu)
    print("Escolha uma opção: ")
    option_selected = int(input("Informe uma opção do menu: "))

    
    if option_selected == 1:
        print(f">> Resulta de Somar: {sum(first_number, second_number)}")
    if option_selected == 2:
        print(f">> Resultado de Mutiplicar: {times(first_number, second_number)}")
    if option_selected == 3:
        print(f">> Resultado de Maior: {bigger(first_number, second_number)}")
    if option_selected == 4:
        first_number = int(input("Primeiro valor: "))
        second_number = int(input("Segundo valor: "))
        print(f">> Novos numeros: {newNumbers(first_number, second_number)}")
    if  option_selected == 5:
        print(">> Voce encerrou o programa!")
        break
    if option_selected not in [1,2,3,4,5]:
        print(">> Digite uma opção novamente!")