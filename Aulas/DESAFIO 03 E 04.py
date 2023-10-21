# DESAFIO 03
n1 = int(input('Vamos fazer uma soma, digite um número: '))
n2 =int(input('Beleza, agora digite mais um: '))
s = n1+n2
print(f'A soma entre {n1} e {n2} é {s}')

#DESAFIO 04
a = input('Agora o próximo passo,digite qualquer coisa: ')
print(f'agora vamos descobrir um pouco sobre {a}')
print(f'{a} é do tipo primitivo',type(a))
print(f'{a} é alfanúmerico? a resposta é:',a.isalnum())
print(f'{a} possui apenas letras?',a.isalpha())
print(f'{a} possui apenas números?',a.isnumeric())
print(f'{a} está todo em letras maiúsculas?',a.isupper())
print(f'{a} está todo em letras minúsculas?',a.islower())
print('Analise finalizada.')