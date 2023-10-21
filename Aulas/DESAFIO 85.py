# DESAFIO 85

dados = [[], []]
for c in range(1,8):
    números = int(input(f'Insira o {c}º número: '))
    if números % 2 == 0:
        dados[0].append(números)
    elif números % 2 != 0:
        dados[1].append(números)
dados[0].sort()
dados[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {dados[0]}'
      f'\nOs valores ímpares digitados foram: {dados[1]}')