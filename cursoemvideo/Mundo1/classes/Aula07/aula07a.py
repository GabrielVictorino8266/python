# Operadores Aritméticos

# + - Adição
# - > Subtração

# Ordem de Precedência (Ordem que precisa ser resolvido.)

# 1-  ()
# 2- **
# 3- * / // %
# 4- + -


n1 = int(input('Insira um valor: '))
n2 = int(input('Insira um segundo valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2

print('A soma vale {}, a multiplicação vale {}, a divisão {}, a divisão inteira {} e a exponenciação {}'.format(s,m,d,di,e), end=' ')
print('Teste de retirar quebra de linha.')

nome = input('Qual o seu nome?')
# print('Prazer em te conhecer {:*^20}'.format(nome))
# print('Prazer em te conhecer {:^20}'.format(nome))

