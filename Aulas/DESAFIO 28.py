# DESAFIO 28
from random import randrange
from time import sleep
a = randrange(0,5)
b = int(input('Pensei em um número entre 0 e 5, em qual número eu pensei?: '))
print('HMMM...')
sleep(1)
if b == a:
    print(f'Você acertou! Eu pensei em {a}!')
else:
    print(f'Vish, errou! Pensei em {a}!')


