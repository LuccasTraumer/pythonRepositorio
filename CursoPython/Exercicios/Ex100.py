from random import randint
lista = []
def sorteio(valores):
    for i in range(0,5,1):
        valores.append(randint(0,20))
        print("Valore: {:.0f} Adicionado.".format(valores[i]))
    print("Todos os Valores são: ",valores)

def somaPar(lista):
    s = 0
    for i in lista:
        if i % 2 ==0:
            s+=i
    print("Soma dos Valores é: {:.0f}".format(s))


sorteio(lista)
somaPar(lista)
