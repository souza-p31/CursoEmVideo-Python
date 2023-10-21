# DESAFIO 105

def notas(*args,sit=False):
    """
    Função que recebe vários valores e retorna a
    quantidade, maior, menor e média das notas.
    Opcional receber a situação de acordo com a média das notas.

    :param args: valores da análise
    :param sit: (opcional) situação levando em consideração a média das notas
    :return: retorna um dicionário com a análise
    """
    print('-'*30)
    aluno = {}
    aluno['qnt_nota'] = len(args)
    aluno['maior_nota'] = max(args)
    aluno['menor_nota'] = min(args)
    aluno['media_notas'] = sum(args) / aluno['qnt_nota']
    if sit == True:
        if aluno['media_notas'] < 5:
            aluno['situação'] = 'Ruim'
        elif 5 <= aluno['media_notas'] <= 7:
            aluno['situação'] = 'Razoável'
        else:
            aluno['situação'] = 'Bom'
    return aluno

# Programa principal
resp = notas(3.5,5,6.5,sit=False)
print(resp)
help(notas)