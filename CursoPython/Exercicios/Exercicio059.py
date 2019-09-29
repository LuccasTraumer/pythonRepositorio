'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1 = float(input('Digite o Primeiro Numero: '))
n2 = float(input('Digite o Segundo Numero: '))
menu = 0
while menu != 5:
    print('-='*20)
    menu = int(input('''
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos Numeros
[5] Sair do Programa
Qual sua Opção: 
'''))
    print('-='*20)
    if menu == 1:
        print('A Soma entre {} e {} é {}'.format(n1,n2,n1+n2))
    elif menu == 2:
        print('A Multiplicação entre {} e {} é {}'.format(n1,n2,n1*n2))
    elif menu == 3:
        if n1 > n2:
            print('O Maior é {} entre {} e {}'.format(n1,n1,n2))
        else:
            print('O Maior é {} entre {} e {}'.format(n2,n2,n1))
    elif menu == 4:
        n1 = float(input('Informe o Primeiro Numero: '))
        n2 = float(input('Informe o Sehundo Numero: '))
    elif menu == 5:
        print('Finalizando..')
    else:
        print('Entrada Invalida')
print('Fim do programa')


