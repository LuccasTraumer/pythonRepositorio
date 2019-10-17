'''
Crie um programa que simule o funcionamento de um caixa eletrônico.No início, pergunte ao usuário qual será o valor a ser sacado
(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('-='*20,end='')
print('BANCO DO TRAUMER',end='')
print('-='*20)
valor = int(input('Que Valoer você quer Sacar?: '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} Cédulas de R$ {ced} ')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('-='*20)
print('Volte Sempre ao Banco do Traumer, Tenha um Bom Dia!')