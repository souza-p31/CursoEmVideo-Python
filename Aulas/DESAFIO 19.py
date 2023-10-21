# DESAFIO 19
import random
print('Vou sortear uma entre quatro pessoas, insira os nomes:\n''')
a = str(input('Insira o nome do primeiro aluno: '))
b = str(input('Ok! Agora do segundo aluno: '))
c = str(input('OK! Agora o terceiro: '))
d = str(input('OK! Por fim, o quarto aluno: '))
e = random.choice([a,b,c,d])
print(f'O sorteado foi {e}.')