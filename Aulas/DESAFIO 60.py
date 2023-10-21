# DESAFIO 60

n = int(input('Insira um número, irei te mostrar o fatorial: '))
resul = 1
cont = 1
while cont <= n:
    resul = resul * cont
    cont = cont + 1
print('''\nUtilizei o código:\n\033[34mwhile cont <= n:
    resul = resul * cont
    cont = cont + 1\033[m''')
print(f'O fatorial de {n} é {resul}, houveram {cont-1} multiplicações.\n')

n1 = int(input('Insira outro número, irei te mostrar o fatorial: '))
result1 = 1
for c in range(n1,0,-1):
    result1 *= c
print('''\nUtilizei o código:\n\033[31mfor c in range(n1,0,-1):
    result1 *= c\033[m''')
print(f'O fatorial de {n1} é {result1}, houveram {n1} multiplicações.')
