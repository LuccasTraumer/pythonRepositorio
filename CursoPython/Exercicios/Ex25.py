'''Crie um Programa que leia o Nome de uma Pessoa e Diga se ela tem Silva no Nome '''

nome = str(input('Digite seu Nome Completo: ')).upper
#boo = '\033[31m Silva \033[m ' in nome
if 'SILVA' in nome:
    print('Tem Silva')
else:
    print('Nao tem Silva')