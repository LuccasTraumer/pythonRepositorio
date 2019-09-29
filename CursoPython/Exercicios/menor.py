n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite outro Numero: '))
n3 = int(input('Digite o ultimo Numero: '))

menor = 0
maior = 0

if n1 < n2 and n1 < n3 :
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior =  n3
print(f'Voce Digitou {n1},{n2} e {n3}, o Maior é {maior} e o Menor {menor}')
