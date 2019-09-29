'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

print('------- ANALISANDO TRIANGULO ---------')


n1 = float(input('Digite o Primeiro Segmento: '))
n2 = float(input('Digite o Segundo Segmento: '))
n3 = float(input('Digite o Terceiro Segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os Segmentos \033[35m Formam \033[m uma Reta ')
    if n1 == n2 and n1 == n3 and n2 == n3:
        print('Triangulo EQUILATERO')

    elif n1 != n2 and n1 != n3 and n2 != n3:
        print('É uma Triangulo ECALENO')

    elif n1 != n2 and n1 == n3:
        print('Triangulo ISOSCELES')
    elif n1 == n2 and n1 != n3:
        print('Triangulo ISÓSCELES')
    elif n2 != n1 and n2 == n3:
        print('Triangulo ISÓSCELES')
    elif n2 == n1 and n2 != n3:
        print('Triangulo ISÓSCELES')
    elif n3 != n1 and n3 == n2:
        print('Triangulo ISOSCELES')
    elif n3 == n1 and n3 != n2:
        print('Triangulo ISOSCELES')

else:
    print('\033[31m Nao Formam \033[m um Triangulo ')
