'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%'''

salar = float(input('Digite o Salário R$: '))
calc15 = (salar*15)/100
calc10 = (salar*10)/100

if salar <= 1250:
    print('Seu Salario erá \033[33m {} \033[m R$ a com o aumento é \033[35m {} \033[m R$'.format(salar,salar+calc15))
if salar >= 1250:
    print('Seu Salario é de \033[33m {} \033[m R$ e com o Aumento será \033[35m {} \033[m R$'.format(salar,calc10+salar))

