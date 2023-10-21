# DESAFIO 49

a = int(input('\033[1mQual tabuada?:\033[m '))
print(f'\033[7mTABUADA DE {a}\033[m')
for c in range (1,11):
    print(f'{a} x {c} = {a*c}')

