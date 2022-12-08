n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
msg = 'A soma entre {} e {} resulta em {}'

print(msg.format(n1, n2, soma))