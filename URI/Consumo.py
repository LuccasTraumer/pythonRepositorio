'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida 
(em Km) e o total de combustível gasto (em litros).
'''

distancia = int(input())
combustivel = float(input())

preco = distancia/combustivel
print("{:.3f} km/l".format(preco))