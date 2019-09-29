'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara.
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
 caso haja uma divisão por 0 ou raiz de numero negativo.
'''

valores = input().split(' ')
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

#Valor do Delta
delta = (b * b) - (4 * a * c)

Parte1X1 = -b + (delta ** (1 / 2))
Parte2X2 = -b - (delta ** (1 / 2))

X1 = Parte1X1 / (2 * a)
X2 = Parte2X2 / (2 * a)

if a <= 0 or delta <= 0:
    print("Impossivel calcular")
else:

    print("R1 = {:.5f}".format(X1))
    print("R2 = {:.5f}".format(X2))