'''
 Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''

#EM WHILE
n = int(input('Digite um Numero paraCalcular o Fatorial: '))
c = n
f = 1
print('Calculando o Fatorial de {}! = '.format(n),end='')
while c > 0:
    print('{} '.format(c),end = '')
    print(' X ' if c > 1 else ' = ', end = '')
    f = f * c
    c-=1
print('{}'.format(f))
