#DESAFIO 27

a = str(input('Insira um nome completo: ')).strip()
b = a.split()
c = len(a.split())
print(f'Primeiro nome: {b[0]}\nÚltimo nome: {b[c-1]}')