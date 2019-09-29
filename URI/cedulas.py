"""
Leia um valor inteiro.
A seguir, calcule o menor número de notas possíveis (cédulas)
no qual o valor pode ser decomposto. As notas consideradas são de
100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
"""

valor = int(input())
cont100 = 0
cont50 = 0
cont20 = 0
cont10 = 0
cont5 = 0
cont2 = 0
cont1 = 0
valoA = valor

while valoA != 0:
    if valoA > 100:
        cont100 +=1
        valoA -= 100
    if valoA >= 50 and valoA < 100:
        cont50 += 1
        valoA -= 50
    if valoA >= 20 and valoA < 50:
        cont20 += 1
        valoA -=20
    if valoA >= 10 and valoA < 20:
        cont10 += 1
        valoA -= 10
    if valoA >= 5 and valoA < 10:
        cont5 += 1
        valoA -= 5
    if valoA >= 2 and valoA < 5:
        cont2+= 1
        valoA -= 2
    if valoA >= 1 and valoA < 2:
        cont1 += 1
        valoA -= 1

print(valor)
print("{} nota(s) de R$ 100,00".format(cont100))
print("{} nota(s) de R$ 50,00".format(cont50))
print("{} nota(s) de R$ 20,00".format(cont20))
print("{} nota(s) de R$ 10,00".format(cont10))
print("{} nota(s) de R$ 5,00".format(cont5))
print("{} nota(s) de R$ 2,00".format(cont2))
print("{} nota(s) de R$ 1,00".format(cont1))
