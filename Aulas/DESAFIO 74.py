# DESAFIO 74
import random
from random import randint

n_aleatorios = (randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5))
print(f'Os valores sorteados foram: ',end='')
for n in n_aleatorios:
    print(f'{n} ',end='')
print(f'\nO maior valor sorteado foi {max(n_aleatorios)}')
print(f'O manor valor sorteado foi {min(n_aleatorios)}')