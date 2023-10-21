# DESAFIO 75

tupla = (int(input('Valor 1: ')),int(input('Valor 2: ')),int(input('Valor 3: ')),int(input('Valor 4: ')))
print(f'Você digitou os valores {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu pela primeira vez na posição {tupla.index(3)+1}')
else:
    print('O número 3 não foi digitado')
cont = 0
for núm in tupla:
    if núm % 2 == 0:
        cont += 1
if cont < 1:
    print('Não houveram números pares')
else:
    print(f'Os números pares foram ',end='')
for núm in tupla:
    if núm % 2 == 0:
        print(f'{núm}, ',end='')

