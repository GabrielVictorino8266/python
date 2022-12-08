# Leia algo pelo teclado e informe o tipo

info = input('Digite algo: ')
numero = info.isnumeric()
letra = info.isalpha()
letranum = info.isalnum()

if numero==True:
    msg = 'você digitou...{0}'
elif letra==True:
    msg = 'você digitou...{1}'
else: 
    msg = 'você digitou...{2}'

print(msg.format('apenas números!', 'apenas letras!', 'números e letras!'))