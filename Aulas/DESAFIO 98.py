# DESAFIO 98
from time import sleep

def contador(inicio, fim, passo):
    print('-='*15
          ,f'\nContagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    if inicio < fim:
        cont1 = inicio
        while cont1 <= fim:
            print(f'{cont1}',end=' ')
            cont1 += passo
        print('FIM!')
    else:
        cont1 = inicio
        while cont1 >= fim:
            print(f'{cont1}',end=' ')
            cont1 -= passo
        print('FIM')
contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)
