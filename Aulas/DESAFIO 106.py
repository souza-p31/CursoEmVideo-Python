# DESAFIO 106

cores = ('\033[m',        # 0 - sem cores
       '\033[0;30;41m',   # 1 - vermelho
       '\033[0;30;42m',   # 2 - verde
       '\033[0;30;43m',   # 3 - amarelo
       '\033[0;30;44m',   # 4 - azul
       '\033[0;30;45m',   # 5 - roxo
       '\033[0;30;47m')   # 6 - branco


def cabeçalho(texto,cor=0):
    tamanho = len(texto)+4
    print(cores[cor],end='')
    print('~'*tamanho)
    print(f'  {texto}')
    print('~'*tamanho)
    print(cores[0],end='')


def pyhelp(ajuda):
    cabeçalho(f"Acessando o manual do comando '{ajuda}'",4)
    print(cores[6],end='')
    função = help(ajuda)
    print(cores[0],end='')

a = ' '
while True:
    cabeçalho('SISTEMA DE AJUDA PYHELP',2)
    a = str(input('Função ou biblioteca > ')).lower()
    if a == 'fim':
        cabeçalho('Até logo!',1)
        break
    else:
        pyhelp(a)


