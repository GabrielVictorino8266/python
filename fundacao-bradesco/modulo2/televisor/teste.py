from funcionalidades import *

tv= Televisor('Sony', 'Sony-123')

controle= ControleRemoto(tv)

controle.sintonizaCanal('GLOBO')
controle.trocaCanal('GLOBO')

print(tv.lista_de_canais)