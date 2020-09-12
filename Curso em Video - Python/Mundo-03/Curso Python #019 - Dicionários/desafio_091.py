# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
# Guarde esses resultados em um dicionário em Python. No final, coloque esse 
# dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

numero = {'jogador1': randint(1, 6),
          'jogador2': randint(1, 6),
          'jogador3': randint(1, 6),
          'jogador4': randint(1, 6)}
ranking = dict()
for k, v in numero.items():
    print(f'{k} jogou {v}')
    sleep(1)
ranking = sorted(numero.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)
