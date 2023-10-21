# DESAFIO 44
print('{:=^40}'.format('Lojas Guanabara'))
a = float(input('Valor do produto: R$'))
print('''Selecione a forma de pagamento
( 1 ) DINHEIRO / CHEQUE
( 2 ) CARTÃO DE CRÉDITO À VISTA
( 3 ) CARTÃO DE CRÉDITO EM ATÉ 2X
( 4 ) CARTÃO DE CRÉDITO EM 3X OU MAIS''')
b = int(input('Modalidade de pagamento: '))
if b == 1:
    print(f'Você irá pagar por esse produto R${a-(a*10/100) :.2f}.')
elif b == 2:
    print(f'Você irá pagar por esse produto R${a-(a*5/100) :.2f}.')
elif b == 3:
    print(f'Você irá pagar o valor normal do produto R${a :.2f}.')
elif b == 4:
    print(f'Você irá pagar por esse produto R${a+(a*20/100) :.2f}.')
else:
    print('Intervalo não permitido.')