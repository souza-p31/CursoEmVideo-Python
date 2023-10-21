# DESAFIO 68
import random

print('=-'*15)
print(' '*2,'VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
cont = 0
while True:
    pc = random.randint(1,10)
    mov1 = int(input('Digite um valor: '))
    mov2 = ' '
    while mov2 not in 'PI':
       mov2 = str(input('Par ou Impar? [P/I]: ')).strip().upper()
    resul = (pc + mov1)
    print('-'*30)
    print(f'Você jogou {mov1} e o PC {pc}, total de {resul}')
    print('-' * 30)
    if mov2 == 'P':
        if resul % 2 == 0:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    if mov2 == 'I':
        if resul % 2 == 1:
            print('Você venceu!')
            cont += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Você teve \033[32m{cont} vitórias\033[m consecutivas!')