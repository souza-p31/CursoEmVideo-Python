# DESAFIO 22
# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras o nome tem (sem considerar os espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Me diga seu nome completo: ')).strip()
print(f'{nome.upper()}')
print(f'{nome.lower()}')
print(len(nome.replace(" ","")))
print(f'{len(nome.split()[0])}')