#Horas-minutos e Segundos

valor = int(input())

horas = 0
minutos = 0
segundos = 0
valorA = valor
contador = segundos
while(contador <= valorA):
    if contador > 0:
        segundos += 1
    if segundos >= 60:
        minutos += 1
        segundos = 0
    if minutos >= 60:
        horas += 1
        minutos = 0
    contador+=1

        

print("{}:{}:{}".format(horas,minutos,segundos))
