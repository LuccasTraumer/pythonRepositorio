'''
 Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo.
Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, 
mostrando a mensagem
'''

data = str(input())
values = data.split(' ')
first = float(values[0])
second = float(values[1])
tercery = float(values[2])

perimetro = first + second + tercery

print(perimetro)