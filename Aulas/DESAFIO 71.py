# DESAFIO 71

print('=*'*15)
print('{:^30}'.format('Seja bem-vindo(a) ao PH Bank'))
print('=*'*15)
saque = int(input('Qual valor você deseja sacar? R$'))
totalsaque = saque
cédula = 50
totalcédula = 0
while True:
    if totalsaque >= cédula:
        totalsaque -= cédula
        totalcédula += 1
    else:
        print(f'Total de {totalcédula} cédulas de {cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcédula = 0
        if totalsaque == 0:
            break
print('=*'*15)
print('{:^30}'.format('Volte sempre!'))