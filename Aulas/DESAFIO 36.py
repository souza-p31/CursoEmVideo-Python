# DESAFIO 36

valor_casa = int(input('\033[7mQual o valor da casa que você vai comprar?\033[m \nR$'))
salário = int(input('\033[7mQual é o seu salário?\033[m \nR$'))
anos = int(input('\033[7mVocê pretende pagar a casa em quantos anos?\033[m\n'))
axm = anos*12
parcela = valor_casa/axm
if parcela > (salário*30/100):
    print(f'Infelizmente seu empréstimo foi negado, pois a parcela do empréstimo ficaria em R${parcela :.2f}\ne esse valor ultrapassa 30% do seu salário.')
else:
    print(f'Seu empréstimo foi aprovado, sua parcela será no valor de R${parcela :.2f}')