'''
Leia a hora inicial e a hora final de um jogo.
A seguir calcule a duração do jogo, sabendo que o mesmo pode começar
em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
'''

data = str(input())
values = data.split(' ')
init_game = int(values[0])
end_game = int(values[1])

if(init_game >= end_game):
    end_game = end_game + 24
    result = end_game - init_game
    print('O JOGO DUROU '+ str(result) + ' HORA(S)')
else:
    result = init_game - end_game
    print('O JOGO DUROU '+ str(result*-1) + ' HORA(S)')


