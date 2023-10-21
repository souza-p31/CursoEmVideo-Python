# DESAFIO 81

num_list = []
count_5 = 0
while True:
    add_num = int(input('Digite um valor: '))
    num_list.append(add_num)
    opção = ' '
    if add_num == 5:
        count_5 += 1
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opção == 'N':
        break
num_list.sort(reverse=True)
print('=-'*30)
print(f'Você digitou {len(num_list)} elementos'
      f'\nOs valores em ordem decrescente são {num_list}')
if count_5 > 0:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não faz parte da lista')


