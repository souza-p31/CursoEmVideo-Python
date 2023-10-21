# DESAFIO 70
print('-'*30)
print('{:^30}'.format('SUPER BARATÃO'))
print('-'*30)
soma = p_mil = m_preço = cont = 0
p_barato = ''
while True:
    produto = str(input('Nome do Produto: ')).upper()
    preço = int(input('Preço: R$'))
    cont += 1
    opçao = ' '
    soma += preço
    while opçao not in 'SN':
        opçao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if preço >= 1000:
        p_mil += 1
    if opçao == 'N':
        break
    if cont == 1 or preço < m_preço:
        m_preço = preço
        p_barato = produto
print('{:-^30}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${soma:.2f}\n'
      f'Temos {p_mil} produtos custando mais de R$1000.00\n'
      f'O produto mais barato foi {p_barato} que custa R${m_preço:.2f}.')