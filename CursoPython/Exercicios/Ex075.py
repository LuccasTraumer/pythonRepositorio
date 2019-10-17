'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No Final Mostre:
A)Quantas Vezes apareceu o valor 9
B)Em que Posição foi digitado o Primeiro Valor 3
C)Quais Foram os Numeros Pares

'''

n1  = int(input('Digite um Numero: '))
n2 = int(input('Digite um Numero: '))
n3 = int(input('Digite um Numero: '))
n4 = int(input('Digite um Numero: '))
lista = (n1,n2,n3,n4)
v3 = lista.index(3)
print(f'Você Digitou os Valores: {n1},{n2},{n3},{n4}')
print(f'Aparaceram {lista.count(9)} Numeros 9')
if 3 in lista:
    print(f'A Posição do Numero 3 é {v3+1}')
if n1 % 2 == 0:
    print(f'{n1},', end='')
if n2 % 2 == 0:
    print(f'{n2}, ',end='')
if n3 % 2 == 0:
    print(f'{n3},',end=' ')
if n4 % 2 == 0:
    print(f'{n4}. ',end='')
    print('São Pares')
else:
    print('Todos são Impares')
