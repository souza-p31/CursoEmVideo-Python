# DESAFIO 72

n = (0, 1, 2 , 3 , 4 , 5, 6, 7, 8, 9, 10, 11, 12 , 13, 14, 15, 16, 17, 18, 19, 20)
n_extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis' , 'dezessete', 'dezoito', 'dezenove', 'vinte')
op_n = ''
while op_n not in n:
    op_n = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {n_extenso[op_n]}')