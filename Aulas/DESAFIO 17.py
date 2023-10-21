#DESAFIO 17
# C²=A²+B²
import math
print('Vou calcular para você a hipotenusa de um triângulo!\n''')
CO=float(input('Qual é o tamanho do cateto oposto? '))
CA=float(input('Qual é o tamanho do cateto adjacente? '))
HS=pow(CO,2)+pow(CA,2)
H=math.sqrt(HS)
print('De acordo com essas informações, a hipotenusa do seu triangulo só pode ser {:.1f}cm'.format(H))