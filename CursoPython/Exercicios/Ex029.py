'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

print('A Velocidade Max é de 80KM/H')
velo = int(input('Digite a Velocidade do Carro: '))
soma = (velo - 80 )
adi = (soma*7)

if velo <= 80:
    print('Vocé está nao paga multa ')

else:
    print('Você pagará \033[34m {} \033[m Reais de Multa'.format(adi))