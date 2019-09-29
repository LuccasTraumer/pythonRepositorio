"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.
"""

valor_indo = float(input("Informe o Valor: "))
valor = valor_indo
#Contador Real
contador100 = 0
contador50 = 0
contador20 = 0
contador10 = 0
contador2 = 0
#Contador Moedas
contador1 = 0
contador050 = 0
contador025 = 0
contador010 = 0
contador005 = 0
contador001 = 0
#Repetição
while valor > 0.0:
    #Repetição Notas
    if valor >= 100:
        contador100+=1
        valor -= 100
    if valor < 100 and valor >= 50:
        contador50+1
        valor -= 50
    if valor >= 20 and valor <50:
        contador20+=1
        valor -= 20
    if valor>= 10 and valor < 20:
        contador10+=1
        valor -= 10
    if valor >= 2 and valor < 10:
        contador2+=1
        valor -= 2
    #Repetição Moedas
    if valor >= 1.00 and valor < 2:
        contador1 +=1
        valor -= 1.00
    if valor >= 0.50 and valor < 1.0:
        contador050+=1
        valor -= 0.50
    if valor >= 0.25 and valor < 0.50:
        contador025 +=1
        valor -= 0.25
    if valor>= 0.10 and valor < 0.25:
        contador010+1
        valor -= 0.10
    if valor >= 0.05 and valor < 0.10:
        contador005 +=1
        valor -= 0.05
    if valor >= 0.01 and valor < 0.05:
        contador001+=1
        valor -= 0.01
    if valor < 0.01:
        break

#Print Notas
print("{} nota(s) de R$ 100.00".format(contador100))
print("{} nota(s) de R$ 50.00".format(contador050))
print("{} nota(s) de R$ 20.00".format(contador20))
print("{} nota(s) de R$ 10.00".format(contador10))
print("{} nota(s) de R$ 2.00".format(contador2))
#Prints Moedas
print("{} nota(s) de R$ 1.00".format(contador1))
print("{} nota(s) de R$ 0.50".format(contador050))
print("{} nota(s) de R$ 0.25".format(contador025))
print("{} nota(s) de R$ 0.10".format(contador010))
print("{} nota(s) de R$ 0.05".format(contador005))
print("{} nota(s) de R$ 0.01".format(contador001))