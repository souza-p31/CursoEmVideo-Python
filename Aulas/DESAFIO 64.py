# DESAFIO 64

n1 = soma = cont = 0
n1 = int(input('Insira um valor para somar [999 para parar]: '))
while n1 != 999:
    soma += n1
    cont += 1
    n1 = int(input('Insira um valor para somar [999 para parar]: '))
print(f'Você somou {cont} números e o resultado da soma foi {soma}.')