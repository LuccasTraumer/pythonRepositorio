'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: - O primeiro valor é maior - O segundo valor é maior - Não existe valor maior, os dois são iguais'''
print('--------------- COMPARANDO DOIS NUMEROS -----------------')

n1 = int(input('Digite o \033[36m PRIMEIRO \033[m Valor: '))
n2 = int(input('Digite o \033[34m Segundo \033[m Valor:'))

if n1 > n2:
    print('O Primeiro Valor é Maior ')
elif n2 > n1:
    print('O Segundo Valor é Maior ')
else:
    print('Os Valor são iguais ')