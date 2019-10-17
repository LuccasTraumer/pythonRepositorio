'''
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''
cont = s = 0
while True:
    n = int(input('Digite um Numero[999 para parar]: '))
    if n != 999:
        cont += 1
        s +=n
    else:
        break
print(f'Voce Digitou {cont} Numeros e a Soma entre eles é { s }')