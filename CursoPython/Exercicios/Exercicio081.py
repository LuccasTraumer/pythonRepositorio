'''
Crie um Programa que vai ler varios Numeros e colocar em uma lista . Depois disso , Mostre :
A) Quantos Numeros foram digitados; B) A lista de Valores,ordenada de forma decrescente ;
C) Se o valor 5 foi digitado e está ou nao na lista.
'''
cont = 0
lista = []
while True:
    num = int(input('Digite um Numero: '))
    lista.append(num)
    cont += 1
    conti = str(input('Quer Continuar[S/N]: ')).upper().strip()[0]
    if conti == 'N':
        break

print(f'Tem {cont} numeros')
print(lista.sort(reverse=True))
if 5 in lista:
    print('Tem o Numero 5')
else:
    print('Não Tem o Numero 5')