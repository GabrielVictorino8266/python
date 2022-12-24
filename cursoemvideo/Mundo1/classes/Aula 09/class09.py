# Fatiamento

frase = "Curso em Vídeo Python"
print(frase[9])

# Output:
# V 
# 

print(frase[9:14])

# Output
# Vídeo

print(frase[9:21:2])

# Output
# VdoPto (Ele pula a cada 2 caracteres)

print(frase[:5])
# Output - Ele inicia do 0 (corresponde a print(frase[0:5]))
# Curso 

print(frase[15:])

# Output
# Python

print(frase[9::3])

# Output
# VePh

# ***************Analise*****************

print(len(frase))
# len -> mostra a qtde de carecteres

print(frase.count('o'))
# Conta quantas letras "O" existem na frase.

print(frase.count("o",0,14))

# Continuar a partir de 16:10