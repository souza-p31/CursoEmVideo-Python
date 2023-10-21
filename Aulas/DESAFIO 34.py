# DESAFIO 34

a = float(input('Me diga seu salário: \033[1;32mR$\033[m'))
if a >= 1250.00:
    print(f'Seu novo salário será \033[1;32mR${a+(a*(10/100)) :.2f}\033[m')
else:
    print(f'Seu novo salário será \033[1;32mR${a+(a*(15/100)) :.2f}\033[m')