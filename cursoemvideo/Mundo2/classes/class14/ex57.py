sex :str = ""
is_sex_valid = False

while not is_sex_valid:
    sex = input("Informe seu sexo: (M/F): ").upper()  
    if sex in ['M', 'F']:
        is_sex_valid = True
    
    answer = "Sexo informado é valido." if is_sex_valid else f"Informe novamente o sexo!"
    print(answer)

# while True:
#     if sex in ['M', 'F']:
#         print("Sexo informado é valido.")
#         break
    
#     sex = input("Informe seu sexo: (M/F)").upper()        
#     print(f"Informe novamente o sexo!")