'''
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('Digite o Seu Peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior Peso é {}'.format(maior))
print('O Menor Peso é {}'.format(menor))