# DESAFIO
N1 = float(input('\033[7mInsira a primeira nota:\033[m '))
N2 = float(input('\033[7mInsira a segunda nota: \033[m'))
M = (N1+N2)/2
print(f'Média {M}')
if M < 5:
    print('REPROVADO!')
elif M > 5 and M < 6.9:
    print('RECUPERAÇÃO!')
elif M > 7:
    print('APROVADO!')