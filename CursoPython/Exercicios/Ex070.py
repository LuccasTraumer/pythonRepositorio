'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
 No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
total = 0
contMil = 0
cont = menor = 0
barato = ''
while True:
    nomeP = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preco do Produto: '))
    cont += 1
    total += preco
    if preco > 1000:
        contMil += 1
    if cont == 1:
        menor = preco
        barato = nomeP
    else:
        if preco < menor:
            menor = preco
            barato = nomeP
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar?: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total da Compra foi {total}')
print(f'Temos o Total de {contMil} Produtos custando Mais de 1000.00')
print(f'O Pruduto mais barato foi {barato}, que custa {menor}')