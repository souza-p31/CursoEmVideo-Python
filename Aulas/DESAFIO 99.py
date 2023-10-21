# DESAFIO 99
from time import sleep

def maior(*args):
    a = len(args)
    print('-='*30)
    print('Analisando os valores passados...')
    if a == 0:
        print(f'Foram informados 0 valores ao todo.'
              f'\nO maior valor informado foi 0.')
    else:
        for c in args:
            print(f'{c} ',end='')
            sleep(0.5)
        print(f'Foram informados {len(args)} valores ao todo.'
              f'\nO maior valor informado foi {max(args)}.')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()