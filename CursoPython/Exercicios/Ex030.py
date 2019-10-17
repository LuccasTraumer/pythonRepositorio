'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

print('--------- \033[35m Programa Par ou Impar \033[m --------------------')
n1 = int(input('Digite um Numero Inteiro: '))
solu = (n1%2)

if solu == 0 :
    print('\033[36m {} \033[m é um Valor é Par '.format(n1))

else:
    print('O Valor é Impar')