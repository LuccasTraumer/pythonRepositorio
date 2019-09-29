#Todas as Letras Maiusculas , frase.upper()
#  Todas as Letras Minusculas, frase.lower()
#  Quantas Letras ao todo(sem considerar espacos) ,
#  Quantas Letras tem o Primeiro Nome. frase.split(0).len()'''


nome = input('Digite o Seu Nome: ').strip()
separa = nome.split()

print('Seu nome em Maiusculo é: \033[35m {}\033[m'.format(nome.upper()))
print('Seu Nome Todo em Minusculo é : \033[33m {}\033[m'.format(nome.lower()))
print('A Quntidade de Letras que tem o seu Nome é(sem os Espaços): \033[35m {} \033[m'.format(len(nome)-nome.count(' ')))
print('Seu Primeiro Nome : \033[34m {} \033[m, letras'.format(separa[0],len(separa[0])))


