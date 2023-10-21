# DESAFIO 84

pessoas = list()
maior = menor = cont = 0
while True:
    dados = list()
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados)
    opção = str(input('Se desejar parar insira \033[1mN\033[m: ')).upper().strip()[0]
    if 'N' in opção:
        break

for p in pessoas:
    if cont == 0:
        cont += 1
        maior = menor = p[:][1]
    if p[:][1] > maior:
        maior = p[:][1]
    else:
        if p[:][1] < menor:
            menor = p[:][1]

print(f'-='*30)
print(f'\nForam cadastradas {len(pessoas)} pessoas'
      f'\nO maior peso foi {maior}kg e pertence a ',end='')
for a in pessoas:
    if a[:][1] == maior:
        print(f'[{a[:][0]}] ',end='')
print(f'\nO menor peso foi {menor}kg e pertence a ',end='')
for b in pessoas:
    if b[:][1] == menor:
        print(f'[{b[:][0]}] ',end='')
