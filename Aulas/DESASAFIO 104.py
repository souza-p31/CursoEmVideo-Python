# DESAFIO 104

def leiaInt(texto):
    checagem = False
    numero = 0
    while True:
        n = str(input(texto)).strip()
        if n.isnumeric():
            checagem = True
            numero = int(n)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if checagem == True:
            break
    return numero

#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')