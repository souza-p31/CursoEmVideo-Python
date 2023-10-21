# DESAFIO 67

while True:
    print('-'*33)
    n = int(input('Quer ver a tabuada de que valor?: '))
    if n <= 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Programa finalizado!')