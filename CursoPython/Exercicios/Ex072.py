'''
Crie um Programa que tenha uma Tupla totalmente preenchida com uma contagem por
extenso, de zero a vinte . Seu Programa deverá ler um Numero pelo Teclado(Entre 0 e 20)
e mostralo por extenso
'''

numeros = ('Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezesete','Dezoito','Dezenove','Vinte')
while True:
    n1 = int(input('Informe um Numero (Entre 0 e 20): '))
    if 0 <= n1 <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'O Numero que Voce digitou foi {n1}, que por extenso é {numeros[n1]}')

