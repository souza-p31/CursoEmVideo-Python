# DESAFIO 65

n1 = cont = soma = maior = menor = 0
opção = 'S'
while opção in 'Ss':
    maior = menor = n1
    n1 = int(input('Insira um valor: '))
    cont += 1
    soma += n1
    opção = str(input('Continuar a somar? [S / N]: ')).strip().upper()[0]
    if opção not in 'SN':
        opção = str(input('Valor inválido, tente novamente [S / N]: '))[0]
        if opção == 'S':
            opção = 'S'
        else:
            opção = 'N'
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
média = soma / cont
print('~'*30)
print(f'Você digitou {cont} números!\nA média deles foi de {média :.0f}, o maior número foi {maior} e o menor foi {menor}.')