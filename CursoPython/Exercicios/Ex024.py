'''Faca um Programa que leia o nome de uma cidade e diga se ela comeca com santo ou nao '''

cidade = input('Digite o Nome da Cidade: ')

boo = 'Santo 'in cidade
if boo == True:
    print('Tem \033[32m Santo \033[m no Nome ')
else:
    print('Nao tem Santo no Nome ')