# DESAFIO 92
import datetime

hoje = datetime.date.today()
ano_atual = datetime.date.strftime(hoje,'20%y')
ano_atual1 = int(ano_atual)
dados = {}

dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual1 - nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
print('-='*30)
      f'\nNome tem o valor {dados["nome"]}'
      f'\nIdade tem o valor {dados["idade"]}'
      f'\nCTPS tem o valor {dados["ctps"]}')
if dados['ctps'] != 0:
    aposentadoria = dados['contratação'] - nascimento + 35
    print(f'Contratação tem o valor {dados["contratação"]}'
          f'\nSalário tem o valor R${dados["salário"]}'
          f'\nAposentadoria tem o valor {aposentadoria}')