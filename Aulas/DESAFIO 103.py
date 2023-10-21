# DESAFIO 103

def ficha(nome='<desconhecido>',gols='0'):
    """
    :param nome:
    :param gols:
    :return:
    """
    print('-'*30)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

n = str(input('Nome jogador: ')).strip()
g = str(input('Número gols: ')).strip()
if n == '' and g == '':
    ficha()
else:
    if n == '':
        ficha(gols=g)
    elif g == '':
        ficha(nome=n)
    else:
        ficha(n,g)