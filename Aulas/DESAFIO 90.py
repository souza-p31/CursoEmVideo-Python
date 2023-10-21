# DESAFIO 90

dado = {}
dado['nome_aluno'] = str(input('Nome: '))
dado['media_aluno'] = float(input(f'Média de {dado["nome_aluno"]}: '))
if dado['media_aluno'] < 5:
    dado['situação'] = 'Reprovado'
else:
    dado['situação'] = 'Aprovado'

print(f'Nome é igual a {dado["nome_aluno"]}'
      f'\nMédia é igual a {dado["media_aluno"]}'
      f'\nSituação é igual a {dado["situação"]}')
