# DESAFIO 91
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador 1': randint(1,6),
             'jogador 2': randint(1,6),
             'jogador 3': randint(1,6),
             'jogador 4': randint(1,6)}
ranking = dict()
print('Valores sorteados:')

for k,v in jogadores.items():
    print(f'O jogador {k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print('-='*30)
for e,v in enumerate(ranking):
    print(f'{e+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)


