'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
n = 0
cont = 0
nu = 0
while n != 999:
    n = int(input('Digite um Numero [999 para parar]: '))
    if n != 999:
        cont+=1
        nu +=n
print('Voce Digitou {} Numeros e a soma é {} '.format(cont,nu))
