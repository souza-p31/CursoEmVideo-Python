# DESAFIO 37
num = int(input('\033[7mInsira um número:\033[m\n'))
conv = int(input('\033[7mOk! Escolha qual será a base de conversão:\033[m\n(1) binário\n(2) octal\n(3) hexadecimal\n'))
if conv == 1:
    print(f'{num} em binário é {bin(num)[2:]}.')
elif conv == 2:
    print(f'{num} em octal é {oct(num)[2:]}.')
elif conv == 3:
    print(f'{num} em hexadecimal é {hex(num)[2:]}.')
