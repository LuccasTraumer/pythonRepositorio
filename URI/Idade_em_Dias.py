#Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

ano_Dias = int(input())
anos = 0
meses = 0
dias = 0
valor = ano_Dias

while valor != 0:
    if valor > 365:
        anos += 1
        valor -= 365
    if valor >= 30 and valor < 365:
        meses += 1
        valor -= 30
    if valor > 0 and valor < 30:
        dias += 1
        valor -= 1




print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{:.0f} dia(s)".format(dias))

"""
contador = 0
while(contador <= ano_Dias):
    if contador > 0:
        dias += 1
    if dias == 30:
        meses += 1
        dias = 0
    if meses == 12:
        anos +=1
        meses = 0
    contador += 1

"""