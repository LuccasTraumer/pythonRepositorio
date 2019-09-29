'''
Crie um programa que faça o computador jogar Jokenpô com você.

'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel','Tesoura')
print(''' Suas Opções :
[0] Pedra
[1] Papel
[2] Tesoura
''')
computador = randint(0,2)
jogador = int(input('Sua Jogada: '))
print('-=' *11)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O Computador Jogou : {}'.format(itens[jogador]))
sleep(1)
print('O Jogador jogou : {}'.format(itens[computador]))
print('-=' * 11)
if computador == 0: # --- Computador Jogou Pedra
    if jogador == 0: # Jogador Jogou Pedra
        print('Empate')
    elif jogador == 1: # Jogador jogou Papel
        print('O Jogador Ganhou ')
    elif jogador == 2: #Jogador jogou Tesoura
        print('Jogador Perdeu ')
    else:
        print('Jogada Invalida')
elif computador == 1: # --- Computador Jogou Papel
    if jogador == 0: # Jogador Jogou Pedra
        print('Jogador Perdeu')
    elif jogador == 1 : # Jogador Jogou Papel
        print('Empate')
    elif jogador == 2 : # Jogador Jogou Tesoura
        print('Jogador Ganhou')
    else:
        print('Jogada Invalida')
elif computador == 2: # --- Computador Jogou Tesoura
    if jogador == 0: # Jogador Jogou Pedra
        print('Jogador Ganhou')
    elif jogador == 1 : # Jogador jogou Papel
        print('Jogador Perdeu')
    elif jogador == 2: # Jogador Jogou Tesoura
        print('Empate')
    else:
        print('Jogada Invalida')