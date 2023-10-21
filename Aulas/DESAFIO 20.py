# DESAFIO 20
import random
print('A seguir insira o nome dos alunos e será retornado a ordem de apresentação\n''')
a = input('Aluno um: ')
b = input('Aluno dois: ')
c= input('Aluno três: ')
d = input('Aluno quatro: ')
e = [a,b,c,d]
print(f'A sequência da apresentação será:',random.sample(e,4))