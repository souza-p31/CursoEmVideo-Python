# DESAFIO 83

expressão = str(input('Digite a expressão: '))
parenteses = list()
for caracter in expressão:
    if caracter == '(':
        parenteses.append(caracter)
    elif caracter == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(caracter)
            break
if len(parenteses) == 0:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')

