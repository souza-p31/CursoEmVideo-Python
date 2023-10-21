# DESAFIO 79
num = []
while True:
    add_num = (int(input('Digite um valor: ')))
    if add_num in num:
        print('Valor duplicado! Não vou adicionar...')
    else:
        num.append(add_num)
        print('Valor adicionado com sucesso...')
    opção = ''
    if opção in 'SNsn':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção in 'N':
        break
num.sort()
print(num)

