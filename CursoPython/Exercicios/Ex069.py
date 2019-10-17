'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
tot18 = 0
totHom = 0
totMul = 0
while True:
    idade = int(input('Digite sua Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totHom += 1
    if sexo == 'F'and idade < 20:
            totMul +=1


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar?: [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de Pessoas com mais de 18 Anos: {tot18}')
print(f'Total de Homens Cadastrados: {totHom}')
print(f'Total de Mulheres com Menos de 20 Anos: {totMul}')