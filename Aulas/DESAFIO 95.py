# DESAFIO 95

jogador = {}
jogadores = []
while True:
    jogador['NOME'] = str(input('Nome do Jogador: '))
    jogador['PARTIDAS'] = int(input(f'Quantas partidas {jogador["NOME"]} jogou? '))
    Gols = []
    jogador['GOLS'] = Gols
    jogador['TOTAL'] = 0
    for c in range(0,jogador['PARTIDAS']):
        Gols.append(int(input(f'Quantos gols na partida {c}? ')))
    for i in jogador['GOLS']:
        jogador['TOTAL'] += i
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    jogadores.append(jogador.copy())
    if opção == 'N':
        break
    else:
        print('-='*30)
print('-='*30)
print(f'{"COD NOME PARTIDAS GOLS TOTAL" :<4}')
print('-'*30)
for e,c in enumerate(jogadores):
    print(f'{e :<4}',end='')
    for v in c.values():
        print(f' {str(v) :<4} ', end='')
    print()
print('-'*30)
while True:
    mostrar_dados = int(input('Mostrar dados de qual jogador?: '))
    if mostrar_dados == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[mostrar_dados]["NOME"]}')
    for e,x in enumerate(jogadores[mostrar_dados]["GOLS"]):
        print(f'No jogo {e} fez {x} gols.')
    print('-'*30)
