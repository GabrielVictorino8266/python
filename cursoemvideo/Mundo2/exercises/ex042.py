# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('='*10)
seg1 = float(input('Digite o valor do Primeiro Segmento: '))
seg2 = float(input('Digite o valor do Segundo Segmento: '))
seg3 = float(input('Digite o valor do Terceiro Segmento: '))

print('Calculando...')

tipoTriangulo=''
# Funcao para analisar os lados.
def verificaLados(seg1,seg2,seg3):
    if seg1!=seg2 and seg1!=seg3 and seg2!=seg3:
        tipoTriangulo='Escaleno'
    elif seg1==seg2 and seg1==seg3 and seg2==seg3:
        tipoTriangulo='EQUILATERO'
    else:
        tipoTriangulo='ISOSCELES'
    return tipoTriangulo

classificacaoTriangulo = verificaLados(seg1,seg2,seg3)

# Compara os segmentos e determina se e triangulo.
if seg1 < (seg2+seg3) and seg2 < (seg1+seg3) and seg3 < (seg2+seg1):
    # Forma Triangulo
    print('FORMA TRIANGULO {}.'.format(classificacaoTriangulo))
else:
    print('NAO FORMA TRIANGULO')