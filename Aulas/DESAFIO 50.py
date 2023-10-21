# DESAFIO 50

soma = 0
for c in range (0, 6):
    a = int(input('Insira um número: '))
    if a % 2 == 0:
        soma += a
print(f'A soma dos números é {soma}.')
