# DESAFIO 66


soma = cont = 0
while True:
    n = int(input(f'Digite o {cont+1}º número da soma ou 999 para parar: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')

