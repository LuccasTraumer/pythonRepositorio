'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input('Iforme o Sexo:[M/F]')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados Invalidos.Por Favor,Informe seu Sexo: [M/F] ')).strip().upper()[0]
print('Seu Sexo {} Registrado com Sucesso'.format(sexo))
