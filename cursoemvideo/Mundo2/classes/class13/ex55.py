PEOPLE = 5
MAIOR_PESO = float()
MENOR_PESO = float()


string = str()

people_weight = list()
for person in range(0, PEOPLE):
    print(f"Informe o peso da {person + 1} pessoa: ", end=" ")
    weight = float(input())

    people_weight.append(weight)
    
    MAIOR_PESO = weight if len(people_weight) >= 2 and people_weight[person - 1] else float()
    string = f"Maior peso lido: {weight}"

    MENOR_PESO = weight if people_weight[person] < weight else float()
    string = f"Menor peso lido: {weight}" if MENOR_PESO else str()

string = "TODOS TEM O MESMO PESO" if MAIOR_PESO == MENOR_PESO else string
print(string)
print(5*"=-")
print("FINALIZADO")
print(5*"=-")