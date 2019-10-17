'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import datetime
now = datetime.now()
now = now.year
contMen = 0
contMai = 0
for c in range (0,7):
    nasc = int(input('Digite o Ano de Nascimento: '))
    ano = (now - nasc)
    if  ano < 18:
        contMen = contMen +1
    else:
        contMai = contMai +1
print('Temos {} Menor de Idade'.format(contMen))
print('Temos {} Maior de Idade'.format(contMai))