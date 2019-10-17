'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import datetime
now = datetime.now()

nasc = int(input('Digite o Ano de seu Nascimento: '))
idade =  now.year - nasc

soma = (idade - 18)
so = (18 - idade)
if idade < 18 :
    print('Quem Nasceu em {} tem {} em {}'.format(nasc,idade,now.year))
    print('Você vai se alistar daqui há {}'.format(so))
    print('E vai se alistar em {}'.format(nasc+18))
elif idade == 18:
    print('Quem Nasceu em {} tem {} em {}'.format(nasc,idade,now.year))
    print('Voce tem que se Alistar \033[31m IMEDIATAMENTE \033[m')


else:
    print('Quem Nasceu em {} tem {} em {}'.format(nasc,idade,now.year))
    print('Voce deveria ter se alistado há {} anos atras'.format(soma))
    print('Voce deveria ter se alistado em {}'.format(nasc+18))
