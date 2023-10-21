#DESAFIO 24
#Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "SANTO".

a = str(input('Insira o nome de uma cidade: ')).strip().upper()
print((a[:5]) == 'SANTO')