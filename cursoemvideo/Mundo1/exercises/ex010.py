#  Quantos reais compram um dólar

# 1 dólar = 5.26

cotacaoAtual = 5.26
real = float(input('Digite a quantia em reais: '))

dolar = real / cotacaoAtual

print('Você pode converter {} reais em {} dólar(es).'.format(real, dolar))