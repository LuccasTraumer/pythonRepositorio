'''
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
n1 = int(input('Digite o  Valor: '))
cont = 0
for c in range(1,n1+1):
    if n1 % c == 0:
        print()
