'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
n1 = int(input('Digite o Valor que quer saber a Tabuada: '))
for c in range(1,11,):
    print('{} X {} é = {}'.format(n1,c,n1*c))