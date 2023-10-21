# DESAFIO 59

n1 = float(input('Insira um valor: '))
n2 = float(input('Ok! Agora insira outro valor: '))
opção = 0

while opção != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('\033[1mOPÇÃO: \033[m'))

    if opção == 1:
        print(n1+n2)
    elif opção == 2:
        print(n1*n2)
    elif opção == 3:
        if n1 > n2:
            print(f'{n1} é maior.')
        else:
            print(f'{n2} é maior.')
    elif opção == 4:
        n1 = int(input('Insira um valor: '))
        n2 = int(input('Ok! Agora insira outro valor: '))
    else:
        print('Opção inválida! Tente novamente!')
print('fim')