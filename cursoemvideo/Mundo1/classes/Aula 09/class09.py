print('''
Hello, Today we'll learn 
more about STRINGS.
''')

# Fatiamento

frase = "Curso em Vídeo Python"

print(frase)
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

print(frase.find('deo'))
# retorna a posição do texto expecificado no método find.

print(frase.find('Android'))

#Retorna -1, ou seja, NÃO ENCONTRADO

print('Curso' in frase)
# O output esperado é True



# TRANSFORMAÇÃO

print(frase.replace('Curso', 'Android'))
# Substitui um texto da string, mas não sobescreve a variável.

print('UPPER CASE: ' + frase.upper())
# Retorna TUDO EM MAISÚCULO
print('lower case: ' + frase.lower())
# Retorna tudo em minúsculo.

print("Captilize" + frase.capitalize())
# Retorna apenas o primeiro caractere de uma string em Maiúsculo

print(frase.title())
# Deicxa a primeira letra de todas as palavras em MAIÚSCULA.

frase2 = "  aprenda python sem espaços  "
print(frase2)
print(frase2.strip())

print(frase2.rstrip())
# Elimina apenas o espaço no final da string.

print(frase2.lstrip())
# Remove o espaço apenas da esquerda.


# ****DIVISÃO****

print(frase.split())
# Cria uma divisão quando encontrar um espaço na string. 
# Ele retorna um array (lista) das palavras separadas.

frase3 = frase.split()
print(' '.join(frase3))
# Junta as papalvras separadas em listas e adiciona o caractere especificado anteriormente ao Join.


# TESTES
fraseTeste = "Curso em Vídeo Python"
dividido = frase.split()
print(dividido[2][3]) #Mostre na segunda palavra a terceira letra