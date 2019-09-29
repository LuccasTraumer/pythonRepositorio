ddd = int(input())

dados = {19:"Campinas",11:"Sao Paulo",61:"Brasilia",71:"Salvador",
         21:"Rio de Janeiro",32:"Juiz de Fora",27:"Vitoria",31:"Belo Horizonte"}

if ddd in dados:
    print(dados[ddd])
else:
    print("DDD nao cadastrado")
