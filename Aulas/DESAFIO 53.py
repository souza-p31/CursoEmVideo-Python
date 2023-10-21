#DESAFIO 53

frase = str(input('Digite sua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1,-1,-1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('Polindromo!')
else:
    print('Não é palindromo!')