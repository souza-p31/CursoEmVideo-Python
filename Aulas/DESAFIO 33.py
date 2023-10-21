# DESAFIO 33
a = int(input('Insira um número: '))
b = int(input('Insira mais um número: '))
c = int(input('Insira mais um número: '))
Lista = [a,b,c]
d = sorted(Lista)
print(d)
print(f'O maior número é \033[1;34;40m{d[2]}\033[m e o menor é \033[1;33;40m{d[0]}\033[m.')
