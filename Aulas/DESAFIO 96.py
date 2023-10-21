# DESAFIO 96

def Area():
    print('Controle de terrenos'
          '\n','-'*15)
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (c): '))
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')
Area()