'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''


frase = str(input('Digite a Frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]

if inverso == junto:
    print('A Palavra {} .É um Palindromo'.format(junto))
else:
    print('Não é um Palindromo , Pois ela Normal é {} e ao contrario é {}'.format(junto,inverso))
