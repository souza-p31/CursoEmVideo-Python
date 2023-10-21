# DESAFIO 31

a = float(input('\033[1mQual a distância da sua viagem em KM?:\033[m '))
if a <= float(200):
    print(f'Sua passagem vai custar \033[1;32mR${0.50*a :.2f}!\033[m')
else:
    print(f'Sua passagem vai custar \033[1;32mR${0.45*a :.2f}!\033[m')