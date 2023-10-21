# DESAFIO 51

n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = n1 + (10-1) * r
for c in range (n1,décimo + 1,r):
    print(c, end = ' ')