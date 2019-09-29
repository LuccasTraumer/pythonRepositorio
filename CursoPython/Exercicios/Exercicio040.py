''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
 - Média abaixo de 5.0: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO'''

n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))

soma = (n1+n2)/2
if soma < 5:
    print('\033[31m REPROVADO \033[m')
elif soma <= 6.9:
    print('\033[33m RECUPERAÇÃO \033[m')
elif soma >= 7 :
    print('\033[34m APROVADO \033[m')