# DESAFIO 35

a = int(input('Qual o tamanho do lado A do triângulo?: '))
b = int(input('Qual o tamanho do lado B do triângulo?: '))
c = int(input('Qual o tamanho do lado C do triângulo?: '))

if a + b > c and a + c > b and b + c > a:
    print('\033[32mSim, da pra formar um triângulo!\033[m')
else:
    print('\033[31mNão, não da pra formar um triângulo!\033[m')