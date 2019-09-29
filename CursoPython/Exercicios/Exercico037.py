'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. '''

print('-------------- \033[36m Conversor de Numero \033[m --------------------')
n1 = int(input('Digite um Numero Qualquer : '))

print('''Escolha uma das Bases de Conversão 
[ 1 ] para \033[33m BINARIO \033[m
[ 2 ] para \033[34m OCTAL \033[m
[ 3 ] para \033[35m HEXADECIMAL \033[m''')
opcao = int(input('Escolha sua Opcão: '))
if opcao == 1:
    print('O Numero {} em \033[33m BINARIO \033[m é {}'.format(n1,bin(n1)[2:]))
elif opcao == 2 :
    print('O Numero {} em \033[34m OCTAL \033[m é {}'.format(n1,oct(n1)[2:]))
elif opcao == 3:
    print('O Numero {} em \033[36m HEXADECIMAL \033[m é {}'.format(n1,hex(n1)[2:]))
else:
    print('\033[31m Opção Invalida \033[m')