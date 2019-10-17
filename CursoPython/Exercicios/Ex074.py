'''
Crie um programa que vai gerar cinco Numeros Aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de Numeros gerados e tambem indique o Menor eo maior valor que estão na tupla
'''
from random import randint
menor = 0
maior = 0
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10),)
tupla = (f'Eu sortei os Valores: {n},')
print(f'Eu sortei os Valores: {n}')
print(f'O Maior Valor é {max(n)} e o Menor é : {min(n)}')

