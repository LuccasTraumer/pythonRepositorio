'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo,
qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.
'''
cont = 0
contS = 0
contI = 0
maior = 0
maioridadehomem = 0
nomevelho = ''
for c in range(0,4):
    cont = cont +1
    print('---- {} Pessoa ------'.format(cont))
    nome = str(input('Digite o Nome: ')).strip()
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    contI = contI + idade
    mediaI = contI/4
    if sexo == 'F' and idade < 20:
        contS = contS + 1
        print()
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
print('O Nome do Homem Mais Velho é {}'.format(nome))
print('{} Mulheres com Menos de 20 Anos'.format(contS))
print('A Média entre eles é: {}'.format(mediaI))
if idade == 1 :
    maior = idade
    print('O Mais Velhor é {}'.format(nome))
'''
Nome do Mais Velho

'''