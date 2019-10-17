'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

'''
EXERCICIO 061

pa = int(input('Informe o Primeiro Numero:  '))
razao = int(input('Informe a Razão: '))
cont = 1
termo = pa
while cont <= 10:
    print('{} > '.format(termo),end='')
    cont += 1
    termo += razao
print('FIM')'''
pri = int(input('Informe o Primeiro Termo: '))
razao = int(input('Informe a Razão: '))
cont = 1
termo = pri
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont < total:
        print('{} > '.format(termo),end='')
        cont += 1
        termo += razao
    print('PAUSE')
    mais = int(input('Quantos Termos a mais Voce quer Ver? '))
print('O Total de Termos foi {}'.format(total))
print('FIM')
