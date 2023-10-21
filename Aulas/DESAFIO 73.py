# DESAFIO 73

times_brasileirão = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo','Athletico PR','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Red Bull','Bragantino','Coritiba','Cuiabá-MT','Ceará','Atletico-GO','Chapecoense')
print('='*30)
print(f'Lista de times do Brasileirão: {times_brasileirão}')
print('='*30)
print(f'Os 5 primeiros são {times_brasileirão[0:5]}')
print('='*30)
print(f'Os 4 ultimos são {times_brasileirão[16:]}')
print('='*30)
print(f'Times em ordem alfabética: {sorted(times_brasileirão)}')
print('='*30)
print(f'O Chapecoense está na {times_brasileirão.index("Chapecoense")+1}ª posição')