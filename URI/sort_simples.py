'''
Leia 3 valores inteiros e ordene-os em ordem crescente.
 No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
'''

values = str(input(''))
value = values.split(' ')
lous = [int(value[0]), int(value[1]), int(value[2])]
lista = [int(value[0]),int(value[1]),int(value[2])]

lista.sort()
for i in lista:
    print(i)
print()
for x in lous:
    print(x)