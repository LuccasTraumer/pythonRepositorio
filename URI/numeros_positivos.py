'''
 Faça um programa que leia 6 valores. Estes valores serão somente negativos ou
positivos (desconsidere os valores nulos). 
 A seguir, mostre a quantidade de valores positivos digitados.
'''

cont = 0
for i in range(0,6):
    value = float(input())
    if(value >= 0):
        cont = cont + 1

print(str(cont) + ' valores positivos')