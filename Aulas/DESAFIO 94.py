# DESAFIO 94

pessoas = []
dados_pessoas = {}

while True:
    dados_pessoas['NOME'] = str(input('Nome: ')).strip()
    dados_pessoas['SEXO'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados_pessoas['IDADE'] = int(input('Idade: '))
    pessoas.append(dados_pessoas.copy())
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
idades = 0
for c in pessoas:
    idades += c['IDADE']
media_idades = idades / len(pessoas)
print(f'- A média de idades é de {media_idades :.2f} anos.')
print('- As mulheres cadastradas foram: ',end='')
for d in pessoas:
    if d['SEXO'] == 'F':
        print(f'{d["NOME"]} ',end='')
print()
print('- Lista de pessoas que estão acima da média:\n')
cont = 0
for e in pessoas:
    if e['IDADE'] > media_idades:
        for k,v in e.items():
            print(f'{k} = {v}; ',end=' ')
            cont += 1
        if cont >= 2:
            print()
print('\n<< ENCERRADO >>')


