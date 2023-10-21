# DESAFIO 82

todos_numeros = []
pares_numeros = []
impares_numeros = []

while True:
    add_num = int(input('Digite um valor: '))
    todos_numeros.append(add_num)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
for n in todos_numeros:
    if n % 2 == 0:
        pares_numeros.append(n)
    elif n % 2 != 0:
        impares_numeros.append(n)
print(f'A lista completa é {todos_numeros}'
      f'\nA lista de pares é {pares_numeros}'
      f'\nA lista de ímpares é {impares_numeros}')
