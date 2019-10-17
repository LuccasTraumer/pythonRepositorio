'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

print('------- ANALISANDO TRIANGULO ---------')


n1 = float(input('Digite o Primeiro Segmento: '))
n2 = float(input('Digite o Segundo Segmento: '))
n3 = float(input('Digite o Terceiro Segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os Segmentos \033[35m Formam \033[m uma Reta ')
else:
    print('\033[31m Nao Formam \033[m um Triangulo ')