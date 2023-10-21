# DESAFIO 101

def voto(nascimento):
    import datetime
    anoAtual = datetime.datetime.today().year
    print('-' * 30)
    idade = anoAtual - nascimento
    if idade >= 16 and idade <= 18 or idade > 70:
        return f'Com {idade}: VOTO FACULTATIVO'
    elif idade < 16:
        return f'Com {idade}: NÃO VOTA'
    else:
        return f'Com {idade}: VOTO OBRIGATÓRIO'


print(voto(1900))


