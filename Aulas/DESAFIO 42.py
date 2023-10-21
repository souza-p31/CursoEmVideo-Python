# DESAFIO 43
print('\033[1;34mInsira abaixo os tamanhos dos lados do triângulo\033[m')
l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))
l4 = sorted([l1,l2,l3])
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 and l1 == l2 and l2 == l3 and l1 == l3:
    print('Com essas dimensões podemos formar um triângulo EQUILÁTERO')
elif l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 and l4[0] == l4 [1] or l4[1] == l4[2]:
    print('Com essas dimensões podemos formar um triângulo ISÓSCELES')
elif l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1 and l1 != l2 and l2 != l3 and l1 != l3:
    print('Com essas dimensões podemos formar um triângulo ESCALENO')
else:
    print('Não da pra formar um triângulo!')