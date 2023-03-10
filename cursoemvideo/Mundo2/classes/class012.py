# Aula 12 do Curso em Video de Python

name = str(input('Qual e o seu nome: '))
# Condicional Simples
if name=='Gabriel':
    print('Bem-vindo, {}'.format(name))
else:
    print('Ola, seu nome e simples.')

# Condicional Aninhada(condicoes dentro de outras.)

if name=="Gabriel":
    print('Nome sensacional')
elif name == "Joao" or name=='Maria' or name=='Paulo':
    print("Seja bem-vindo, {}".format(name))
else:
    print('Tenha um bom dia, {}'.format(name))

    