# DESAFIO 58

from random import randrange
from time import sleep

pc = randrange(0,10)
tentativas = 1
jogador = int(input('\033[7mPensei em um número de 0 a 10, em qual número pensei?:\033[m '))
while jogador != pc:
    jogador = int(input('\033[7mErrou! Tente novamente!:\033[m '))
    tentativas += +1
    if jogador > pc:
        print('Menos...')
    else:
        print('Mais...')
print(f'Acertou! Você apenas precisou de {tentativas} tentativas.')
