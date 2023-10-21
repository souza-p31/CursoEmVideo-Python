# DESAFIO 76

produtos_preços = ('Lápis',1.75,'Borracha',2.00,'Caderno',
                   15.90,'Estojo',25.00,'Transferidor',4.20,
                   'Compasso',9.99,'Mochila',120.32,
                   'Canetas',22.30,'Livros',34.90)
print('-'*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-'*30)
for p in range(0,len(produtos_preços)):
    if p % 2 == 0:
        print(f'{produtos_preços[p] :.<20}R$',end='')
    if p % 2 != 0:
        print(f' {produtos_preços[p] :>6.2f}')
print('-'*30)
