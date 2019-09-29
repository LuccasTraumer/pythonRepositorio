'''Faca um Programa que leia um numero de 0 a 9999 e mostre na tela cada um dos gigitos separados
Ex: 1834
4 Unidades , 3 Dezenas , 8 Centenas , 1 Milhar
'''

numero = input('Digite um Numero de O a 9999: ')


print('\033[31m {} \033[m,Unidades '.format(numero[3]))
print('\033[32m {} \033[m,Dezenas '.format(numero[2]))
print('\033[33m {} \033[m, Centenas '.format(numero[1]))
print('\033[34m {} \033[m, Milhar '.format(numero[0]))