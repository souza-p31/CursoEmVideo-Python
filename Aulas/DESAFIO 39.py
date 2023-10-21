# DESAFIO 39
from datetime import date
idade = int(input('\033[1minsira o ano em que você nasceu:\033[m '))
ano = date.today().year
if (ano-idade) == 18:
    print('Já está na hora de se alistar!')
elif (ano-idade) < 18:
    print('Você ainda vai se alistar!')
elif (ano-idade) > 18:
    print('Já passou o tempo de se alistar!')
