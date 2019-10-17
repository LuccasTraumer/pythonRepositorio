'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor'''

n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite o Segundo Numero: '))
n3 = int(input('Digite o Terceiro Numero: '))

# Verificando o Menor Valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando Maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O Menor Valor é : \033[36m {}\033[m '. format(menor))
print('O Maior Valor é : \033[34m {}\033[m '.format(maior))
