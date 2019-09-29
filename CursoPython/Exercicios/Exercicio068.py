'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''
from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR ')
print('-='*20)
cont = 0
computador = randint(1,10)
while True:
    player = int(input('Diga um Valor: '))
    escolha = str(input('PAR ou IMPAR: ')).strip().upper()[0]
    soma = computador + player
    if soma % 2 == 0:
        print(f'Voce Jogou {player} e o Computador jogou {computador} que deu {soma} e é PAR')
    else:
        print(f'Voce Jogou {player} e o Computador Jogou {computador} que deu {soma} e é IMPAR ')
    if escolha == 'P' and soma % 2 == 0 or escolha ==  'I' and soma % 2 == 1:
        print('YOU WIN')
    elif escolha != 'P' and soma % 2 == 0 or escolha == 'I' and soma % 2 == 1:
        print('YOU LOSE')
        break
    cont += 1
print(f'GAME OVER VOCE VENCEU {cont} VEZES')