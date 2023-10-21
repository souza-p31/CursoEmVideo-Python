# DESAFIO 18
import math
print('Me diga um ângulo, e eu te direi o seno, o cosseno e a tangente dele:\n''')
ângulo = int(input('Insira um ângulo: '))
a = math.radians(ângulo)
seno = math.sin(a)
cosseno = math.cos(a)
tangente = math.tan(a)
print(f'O seno de {ângulo} é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}.')