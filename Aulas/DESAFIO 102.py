# DESAFIO 102

def fatorial(n,show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    valor = 1
    if show == False:
        for c in range(n,1,-1):
            valor *= c
    else:
        for c in range(n,1,-1):
            valor *= c
            print(f'{c} x',end=' ')
        print('1 = ',end='')
    return valor

#Programa principal
print(fatorial(5,show=True))
help(fatorial)

