# DESAFIO 41
from datetime import date
a = int(input('\033[1mInsira o ano em que você nasceu:\033[m\n'))
ano = date.today().year
idade = ano-a
print(f'Sua idade é {idade}')
print('Sua categoria é:')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
elif idade > 25:
    print('MASTER')
else:
    print('Intervalo inválido')