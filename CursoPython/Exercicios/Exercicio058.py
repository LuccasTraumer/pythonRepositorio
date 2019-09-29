'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
computador = randint(0,10)
print('''Sou Seu Computador...
Acabei de Pensar em Numero de 0 a 10
Voce Consegue Advinhar ?
''')
n = int(input('Qual o Seu Palpite? :'))
cont = 0

if n <= 10:
    while n != computador:
        cont = cont + 1
        n = int(input('Qual seu Palpite? : '))
        if n < computador:
            print('Mais , Tente Novamente.')
        else:
            print('Menos, Tente Novamente.')
else:
    print('Numero Invalido')
print('Voce Acertou com {} Tentativas.Parabens'.format(cont))
