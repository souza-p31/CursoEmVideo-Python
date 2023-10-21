# DESAFIO 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

n = int(input('Insira um número de 0 a 9999: '))
a = str(n)
print(f'{a} possui: \n'
      f'{a[0]} milhar(es)\n'
      f'{a[1]} centena(s)\n'
      f'{a[2]} dezena(s)\n'
      f'{a[3]} unidade(s)\n')