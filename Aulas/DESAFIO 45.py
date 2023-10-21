# DESAFIO 45
from random import choice
lista = ['PEDRA','PAPEL','TESOURA']
PC = choice(lista) #O PC FAZ A ESCOLHA DELE
print('\033[1;35mVamos jogar pedra, papel e tesoura. \nConsegue me vencer?\033[m')
PLAYER = str(input('''Qual será sua jogada?
PEDRA, PAPEL OU TESOURA?\n''')).upper().strip()
if PLAYER == PC:
    print(f'Eu escolhi \033[1;31m{PC}\033[m e você \033[1;32m{PLAYER}\033[m, deu empate. Vamos de novo?.')
elif PLAYER == 'PEDRA' and PC == 'TESOURA' or PLAYER == 'TESOURA' and PC == 'PAPEL' or PLAYER == 'PAPEL' and PC == 'PEDRA':
    print(f'Eu escolhi \033[1;31m{PC}\033[m, você me venceu! Vamos de novo?.')
elif PLAYER == 'PEDRA' and PC == 'PAPEL' or PLAYER == 'PAPEL' and PC == 'TESOURA' or PLAYER == 'TESOURA' and PC == 'PEDRA':
    print(f'Eu escolhi \033[1;31m{PC}\033[m. te venci! Vamos de novo?.')
else:
    print('Intervalo não permitido.')