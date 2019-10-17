'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
print('-='*20)
print('\033[m35 TABUADA \033')
print('-='*20)
while True:
    n = int(input('Tabuada de Qual Valor: '))
    print('-='*30)
    if n > 0:
        for c in range(1,11):
            print(f'{n} X {c} = {n*c}')
    if n < 0:
        print('Programa Finalizado')
        break
    print('-='*30)

