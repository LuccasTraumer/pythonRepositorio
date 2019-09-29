'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uam Frase: ')).upper()
frase.strip()
quant =  frase.count('A')
maius = frase.find('A')

print("A Letra A aparece \033[31m{} \033[m Vezes".format(quant))
print('A Primeira Letra A Aparece na Posica \033[32m {} \033[m'.format(maius))
print('A Ultima vez em que aparece \033[33m {} \033[m'.format(frase.rfind('A')))