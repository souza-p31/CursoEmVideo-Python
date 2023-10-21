# DESAFIO 32

a = int(input('\033[7mMe diga um ano, e eu direi se ele é bissexto:\033[m '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('\033[1;32mAno bissexto!\033[m')
else:
    print('\033[1;31mNão é um ano bissexto!\033[m')