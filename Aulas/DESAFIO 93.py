# DESAFIO 93

jogador = {}

jogador['NOME'] = str(input('Nome do Jogador: '))
jogador['PARTIDAS'] = int(input(f'Quantas partidas {jogador["NOME"]} jogou? '))
Gols = []
jogador['GOLS'] = Gols
jogador['TOTAL'] = 0

for c in range(0,jogador['PARTIDAS']):
    Gols.append(int(input(f'Quantos gols na partida {c}? ')))
print('-='*30)
for i in jogador['GOLS']:
    jogador['TOTAL'] += i
print(jogador)
print('-='*30)
print(f'O campo nome tem o valor {jogador["NOME"]}'
      f'\nO campo gols tem o valor {jogador["GOLS"]}'
      f'\nO campo total tem o valor {jogador["TOTAL"]}')
print('-='*30)
print(f'O jogador {jogador["NOME"]} jogou {jogador["PARTIDAS"]} partidas.')
for e,g in enumerate(jogador["GOLS"]):
    print(f'   => Na partida {e}, fez {g} gols.')
print(f'Foi um total de {jogador["TOTAL"]} gols.')
