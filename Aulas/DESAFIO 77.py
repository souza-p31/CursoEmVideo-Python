# DESAFIO 77

palavras = ('APRENDER','PROGRAMAR','LINGUAGEM',
            'PYTHON','CURSO','GRATIS','ESTUDAR',
            'PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR',
            'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra in 'AEIOU':
            print(f'{letra} ',end='')