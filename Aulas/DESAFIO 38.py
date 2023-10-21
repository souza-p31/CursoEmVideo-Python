# DESAFIO 38
n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
if n1>n2:
    print(f'{n1} é maior que {n2}.')
elif n2>n1:
    print(f'{n2} é maior que {n1}.')
elif n1 == n2:
    print('Não existe valor maior, os dois números são iguais.')
else:
    print('Valor inválido.')