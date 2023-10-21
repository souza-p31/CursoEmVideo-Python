# DESAFIO 97

def mensagem(msg):
    tamanho = len(msg) + 4
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)
mensagem('Eu sou muito sinistro no Python')