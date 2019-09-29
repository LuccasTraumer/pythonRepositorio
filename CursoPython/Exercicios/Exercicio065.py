'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''


n = cont = soma = max = min = media = 0
r = ''
while r != 'N':
    n = int(input('Digite um Numero: '))
    r = str(input('Quer Continuar? [S/N]: ')).upper().strip()[0]
    cont += 1
    soma += n
    media = (soma/cont)
    if n > max: max = n
    if cont == 0: min = n
    if n < min: min = n
print('Voce Digitou {} Numeros , Média é {}'.format(cont,media))
print('O Maior Valor foi {} e o Menor foi {}'.format(max,min))





'''
n = cont = soma = media = max = min = 0
c = ''
while c != 'N':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N]: ')).strip().upper()
    soma = soma + n
    if n > max: max = n
    if cont == 0: min = n
    elif n < min: min = n
    cont = cont + 1
    media = soma / cont
print('Você digitou {} números e a média foi {:.2f} '.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(max, min))
'''