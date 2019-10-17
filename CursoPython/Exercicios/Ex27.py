'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input('Digite seu Nome: ').strip())
separo = nome.split()
sl = separo.__len__()

#print(sl)
print('Seu Primeiro Nome é:\033[31m{}'.format(separo[0]))
print('Seu Ultimo Nome é: \033[32m{}'.format(separo[-1]))