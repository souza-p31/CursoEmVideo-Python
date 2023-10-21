# DESAFIO 52

num = int(input('Insira um número: '))
count = 0
for c in range (1,num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        count = count + 1
    else:
        print('\033[31m', end='')
    print(f'{c}\033[m ', end='')
if count == 2:
    print(f'\nO número {num} foi divisível {count} vezes, portanto é um número primo.')
else:
    print(f'\nO número {num} foi divisível {count} vezes, portanto não é um número primo.')