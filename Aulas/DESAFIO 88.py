# DESAFIO 88
from random import randint
import time

jogos = []
jogo = []

print('-'*20)
print(f'{"JOGA NA MEGA CENA" :^20}')
print('-'*20)
qnt_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3,f' SORTEANDO {qnt_jogos} JOGOS','-='*3)
for c in range(0,qnt_jogos):
    for a in range(0,6):
        número = (randint(0,61))
        if número not in jogo:
            jogo.append(número)
        else:
            while número in jogo:
                número = (randint(0, 61))
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
for e,j in enumerate(jogos):
    time.sleep(0.5)
    print(f'Jogo {e+1}: {j}')
    time.sleep(0.5)
print('-='*3,' < BOA SORTE! > ','-='*3)