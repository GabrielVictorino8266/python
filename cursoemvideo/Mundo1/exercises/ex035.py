# Desenvolva um 
# programa que leia o comprimento de três retas e diga ao usuário se 
# elas podem ou não formar um triângulo.
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

print(' ')

primeiroSegmento = float(input('Primeiro Segmento: '))
segundoSegmento = float(input('Segundo Segmento: '))
terceiroSegmento = float(input('Terceiro Segmento: '))


# if segundoSegmento >= primeiroSegmento and segundoSegmento >= terceiroSegmento:
#     # O segundo é o maior de todos
#     seraTriangulo = primeiroSegmento + terceiroSegmento
#     if seraTriangulo >= segundoSegmento:
#         print('É triângulo.')
# elif terceiroSegmento >= primeiroSegmento and terceiroSegmento >= segundoSegmento:
#     # o tericeiro é o maior
#     seraTriangulo = primeiroSegmento + segundoSegmento
#     if seraTriangulo >= terceiroSegmento:
#         print('É triângulo.')
# else:
#     # o primeiro é o maior
#     seraTriangulo = segundoSegmento + terceiroSegmento
#     if seraTriangulo >= primeiroSegmento:
#         print('É triângulo.')

# print('NÃO FORMA TRIÂNGULO')
if primeiroSegmento < segundoSegmento + terceiroSegmento and segundoSegmento < primeiroSegmento + terceiroSegmento and terceiroSegmento < segundoSegmento + primeiroSegmento:
    print('\033[4;35;42m Os segmentos FORMAM um triângulo.\033[m')
else:
    print('\033[7;31;41m Os segmentos NÃO FORMAM um triângulo.\033[m')