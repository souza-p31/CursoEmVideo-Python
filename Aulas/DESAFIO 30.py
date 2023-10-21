# DESAFIO 30

a = int(input('\033[4mInsira um número:\033[m '))
b = a%2
if b == 0:
    print('\033[1mEsse número é par!\033[m')
else:
    print('\033[7mEsse número é ímpar!\033[m')