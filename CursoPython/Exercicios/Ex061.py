'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

'''
EXERCICIO051
termo = int(input('Digite o Termo: '))
razao = int(input('Digite a Razao: '))
decimo = termo + (10 - 1) * razao
for c in range(termo,decimo,razao):
    print('{}'.format(c),end = ' > ')
print('Acabou')
'''
pa = int(input('Informe o Primeiro Numero:  '))
razao = int(input('Informe a Razão: '))
cont = 1
termo = pa
while cont <= 10:
    print('{} > '.format(termo),end='')
    cont += 1
    termo += razao
print('FIM')