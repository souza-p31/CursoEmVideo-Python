#DESAFIO 26

a = str(input('Insira uma palavra: ')).strip()
b = a.upper()
print(b.count('A'))
print(b.find('A')+1)
print(b.rfind('A')+1)