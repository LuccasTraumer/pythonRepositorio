'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
'''
s = 0
cont = 0
for c in range(0,6):
    n1 = int(input('Digite o Valor: '))
    if n1 % 2 == 0:
        s+=n1
        cont = cont + 1
print('Apareceu {} Numeros Pares e a Soma deles é {}'.format(cont,s))

