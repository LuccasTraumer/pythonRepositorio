'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. '''

dist = int(input('Digite a Distância da Viagem: '))

soma = (dist * 0.50)
els = (dist* 0.45)
if dist <= 200:
    print('Voce Pagara \033[31m {} \033[m pela viagem de \033[35m {} \033[m KM.'.format(soma,dist))
else:
    print('Voce Pagara \033[31m {} \033[m por \033[35m {} \033[m KM'.format(els,dist))