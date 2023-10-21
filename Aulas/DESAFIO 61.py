# DESAFIO 62

p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
resul = p1
c = 1
while c <= 10:
    print(f'{resul} -> ', end='')
    c += +1
    resul += +r
print(resul)

#an = a1+(n-1)*r