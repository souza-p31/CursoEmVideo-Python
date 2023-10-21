# DESAFIO 63

print('~'*30)
print('Sequência de Fibonacci')
print('~'*30)
termos = int(input('Quantos termos?: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} - {t2} - ', end='')
while cont <= termos:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    cont += +1
    t1 = t2
    t2 = t3
print('FIM')


