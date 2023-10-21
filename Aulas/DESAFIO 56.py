# DESAFIO 56
gmulher = 0
nnomenome = 0
nomenome = 0
mevelho = 0
mavelho = 0
media_idade = 0
for a in range (1,5):
    nome = str(input(f'Nome da {a}ª pessoa: ')).strip().upper()
    idade = int(input(f'Idade da {a}ª pessoa: '))
    genero = str(input(f'Gênero da {a}ª pessoa: ')).strip().upper()
    print('OK!')

    media_idade += + idade

    if genero == 'FEMININO' and idade < 20:
        gmulher += + 1

    if a == 1 and genero != 'FEMININO':
        mavelho = idade
        mevelho = idade
        nomenome = nome
        nnomenome = nome
    else:
        if idade>mavelho and genero != 'FEMININO':
            mavelho = idade
            nomenome = nome
        if idade<mevelho and genero != 'FEMININO':
            mevelho = idade
            nnomenome = nome

print(f'A média das idades é {media_idade/a}.')
print(f'O mais velho tem {mavelho} anos e seu nome é {nomenome}.')
print(f'{gmulher} mulher tem menos de 20 anos.')