'''
Crie um Programa onde o usuario possa digitar varios valores Numericos e Cadastre-os em uma lista .
Caso o Numero ja exista la dentro , ele nao será adicionado .
 No final , serão exibidos todos os Valores unicos digitados, em ordem crescente
 '''
lista = []
while True:
    num = int(input('Informe um Numero: '))
    continu = str(input('Quer Continuar[S/N]: ')).upper()[0]
    numlist = num
    lista = [numlist]
    if num in lista:
        print('Over')
    if continu == 'nN':
        break

