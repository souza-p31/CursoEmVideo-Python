# DESAFIO 62

p = int(input('Primeiro termo PA: '))
r = int(input('Razão PA: '))
c = 1
mais = 10
a = 0
total = 0
result = p

while mais != 0:
    total += +mais
    while c <= total:
        print(f'{result} -> ', end='')
        result += +r
        c += +1
    print('pausa')
    mais = int(input('Você quer mais quantos termos?: '))
print(f'Progressão finalizada com {total} termos mostrados.')
