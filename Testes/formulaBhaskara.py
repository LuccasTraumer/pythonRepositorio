'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da
equação de Bhaskara. Se não for possível calcular as raízes,
mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.
'''
import math

valores = input().split(' ')
a = float(valores[0])
b = float(valores[1])
c =  float(valores[2])
delta = b*b - 4*a*c
raiz =  math.sqrt(delta)
x1 = (-b + raiz)*2
x2 = (-b - raiz)*2
print(x1)
print(x2)
