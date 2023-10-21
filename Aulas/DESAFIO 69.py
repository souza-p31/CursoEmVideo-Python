# DESAFIO 69

dezoito = homem = mulher = 0
while True:
    print('-' * 30)
    print(' ' * 4, 'CADASTRE UMA PESSOA')
    print('-' * 30)
    idades = int(input('Qual a idade?: '))
    generos = ' '
    opção = ' '
    while generos not in 'MF':
        generos = str(input('Qual gênero? [M/F]: ')).strip().upper()[0]
    print('-' * 30)
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if idades >= 18:
        dezoito += 1
    if generos == 'M':
        homem += 1
    if idades < 20 and generos == 'F':
        mulher += 1
    if opção == 'N':
        break
print('\n===== FIM DO PROGRAMA =====')
print(f'\nTOTAL DE PESSOAS COM MAIS DE 18 ANOS: {dezoito}.\nAO TODO TEMOS {homem} HOMENS CADASTRADOS.\nE TEMOS {mulher} MULHERES COM MENOS DE 20 ANOS.')

