'''
Faça um programa que leia três valores e apresente o maior dos três valores 
lidos seguido da mensagem “eh o maior”
'''

valores = input().split(' ')
valor1 = int(valores[0])
valor2 = int(valores[1])
valor3 = int(valores[2])

if valor1 > valor2 and valor1 > valor3:
    print(valor1,"eh o maior")
if valor2 > valor1 and valor2 > valor3:
    print(valor2,"eh o maior")
if valor3 > valor1 and valor3 > valor2:
    print(valor3,"eh o maior")