# DESAFIO 87

matriz = [[],[],[],[]]
cont = cont1 = 0
for c in range(0,9):
    add = int(input(f'Digite o valor para [{cont1}, {cont}]: '))
    matriz[:][cont1].append(add)
    cont += 1
    if cont > 2:
        cont1 += 1
        cont = 0
    if add % 2 == 0:
        matriz[:][3].append(add)

soma_terceira_coluna = matriz[:][0][2] + matriz[:][1][2] + matriz[:][2][2]
soma_pares = sum(matriz[:][3])
maior_segunda_linha = max(matriz[:][1])

print(f'-='*30)
print(f'[ {matriz[:][0][0]} ] [ {matriz[:][0][1]} ] [ {matriz[:][0][2]} ]'
      f'\n[ {matriz[:][1][0]} ] [ {matriz[:][1][1]} ] [ {matriz[:][1][2]} ]'
      f'\n[ {matriz[:][2][0]} ] [ {matriz[:][2][1]} ] [ {matriz[:][2][2]} ]')
print('-='*30)
print(f'A soma dos valores pares é {soma_pares}'
      f'\nA soma dos valores da terceira coluna é {soma_terceira_coluna}'
      f'\nO maior valor da segunda linha é {maior_segunda_linha}')

