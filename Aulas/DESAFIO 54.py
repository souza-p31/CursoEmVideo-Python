# DESAFIO 54

from datetime import date
ano = date.today().year
contador = 0
for c in range (1,7+1):
    nascimento = int(input(f'{c}a data: '))
    if ano - nascimento >= 18:
        contador += +1
print(f'{contador} alcançaram a maioridade.')