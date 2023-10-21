# DESAFIO 89

alunos = []

while True:
    dados = []
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    dados.append(nome),dados.append(nota_1),dados.append(nota_2),dados.append(media)
    alunos.append(dados)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break

print('-='*10)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>5}')
print('-'*20)
for e,a in enumerate(alunos):
    print(f'{e:<4}{a[:][0]:<10}{a[:][3]:>5.1f}')
print('-'*20)

while True:
    notas_aluno = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if notas_aluno == 999:
        break
    if notas_aluno >= len(alunos):
        notas_aluno = int(input('No. inválido, tente novamente (999 para interromper): '))
    if notas_aluno != 999:
        print(f'Notas de {alunos[:][notas_aluno][0]} são {alunos[:][notas_aluno][1],alunos[:][notas_aluno][2]}')
        print('-'*20)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')

