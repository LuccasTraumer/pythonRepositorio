'''
Crie um Programa onde o usuario possa dgitar cinco valores Numericos e Cadastre-os em uma lista,
já na Posiçãao correta de inserção(sem usar o sort()). No Final, Mostre a lista ordenada na tela
'''
lista = []
mai  = 0
men = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um Valor para a Posição {c}: ')))
    if c == 0:
        mai = men = lista[0]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[0] < men:
            men = lista[c]
print('-=*'*30)
print(f'Sua Lista é {lista}')
print(f'O Maior Valor é {mai} e o Menor é {men}')