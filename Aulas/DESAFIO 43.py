# DESAFIO 44
peso = float(input('Insira seu peso em KG: '))
altura = float(input('Insira sua altura em M: '))
imc = peso/(altura*altura)
print(f'\033[1mseu IMC é {imc :.2f}.\033[m')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc > 18.5 and imc <= 25:
    print('PESO IDEAL')
elif imc > 25 and imc <= 30:
    print('SOBREPESO')
elif imc > 30 and imc <= 40:
    print('OBESIDADE')
elif imc > 40:
    print('OBESIDADE MÓRBIDA')
else:
    print('INTERVALO NÃO PERMITIDO!')