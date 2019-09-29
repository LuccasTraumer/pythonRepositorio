'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

print('--------------------\033[32m ANO BISSEXTO \033[m----------------')

ano = int(input('Digite o Ano: '))
soma = ano%4
if soma == 0:
    print('O Ano \033[34m {}\033[m é BISSEXTO , sendo assim tem \033[36m 366 \033[m Dias'.format(ano))
else:
    print('O Ano não é BISSEXTO.')