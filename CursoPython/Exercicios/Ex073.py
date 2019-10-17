'''
Crie uma Tupla preenchida com os 20 Primeiros Colocados da Tabela do Campeonato Brasileiro de Futebol,na ordem de colocação
Depois Mostre:
A) Apenas os 5 Primeiros colocados;
B) Os ultimos colocados na tabela;
C)Uma Lista com os ultimos times em ordem alfabetica;
D)Em que Posição está o Time Chapecoence
'''
times = ('Atletico-MG','Flamengo','Corinthias','Palmeiras','Fluminense','America-MG','São Paulo','Gremio','Vasco','Internacional','Botafogo','Sport','Cruzeiro','Vitoria','Santos','Chapecoence','Atletico-PR','Bahia','Ceara','Parana')
c = times
print('-='*20)
print(f'Lista de Times do Brasileirão: {times} ')
print('-='*20)
print(f'Os 5 Primeiros são {times[0:5]}')
print('-='*20)
print(f'Os 4 Ultimos são: {times[16:20]}')
print('-='*20)
print(f'Times em Ordem Alfabetica: {sorted(times)}')
print('-='*20)
print(f"A Chapecoence está na 16º posição")
print('-='*20)