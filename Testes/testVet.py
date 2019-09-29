'''
Tamnho do Vet
Colocar os dados no Vet e somar os dadso dentro
'''
tamanhoVet = int(input("Tamnho do Vet: "))
cont = 0
dados = []
while cont < tamanhoVet:
    dados.append(int(input("Valor {}: ".format(cont))))
    cont += 1
print("A Soma é: {}".format(sum(dados)))
