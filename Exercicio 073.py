#Exercício Python #073 - Tuplas com Times de Futebol

clas = ('Palmeiras', 'Corinthians', 'Atlético-PR', 'Atlético-MG', 'Internacional', 'Fluminense', 'Botafogo', 'Santos', 'São Paulo', 'Bragantino', 'Avaí', 'Atlético-GO', 'Ceará', 'Flamengo', 'Coritiba', 'América-MG', 'Goiás', 'Cuiabá', 'Fortaleza', 'Juventude')

print('=' * 40)

print(f'Classificação do Brasileiro ==> {clas} ')

print('=' * 40)

print(f'Os cinco primeiros são ==> {clas[0:4]}')

print('=' * 40)

print(f'Os quatro últimos são ==> {clas[16:]}')

print('=' * 40)

print(f'Times em ordem alfabética: {sorted(clas)}')

print('=' * 40)

print(f'O Corinthians está na {clas.index("Corinthians") + 1}ª posição')

print('=' * 40)