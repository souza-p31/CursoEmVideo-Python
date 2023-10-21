#DESAFIO 55
menor = 0
maior = 0
for a in range (1,6):
    pesos = float(input(f'Peso da {a}ª pessoa: '))
    if a == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos>maior:
            maior=pesos
        if pesos<menor:
            menor=pesos
print(f'O maior peso foi {maior}KG e o menor foi {menor}KG.')
