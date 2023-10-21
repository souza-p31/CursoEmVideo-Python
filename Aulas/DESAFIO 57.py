# DESAFIO 57

sexo = str(input('Qual é o seu sexo [M / F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Entrada inválida, digite seu sexo [M / F]: ')).strip().upper()[0]

print(f'Ok! Sexo {sexo} registrado!')