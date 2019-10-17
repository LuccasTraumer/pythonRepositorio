'''Escreva um programa que faça o computador "pensar" em
um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
 escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
import math

random = (0,5)
n1 = int(input('Digite um Numero de 0 a 5 : '))

if n1 == random:
    print('Parabens você acertou , o Numero era :\033[32m {}'.format(random))
else:
    print('Você Errou , Está sem sorte')