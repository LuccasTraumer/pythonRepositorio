lista = []
mai = 0
men = 0
for c in range(0,5):
    lista.append( int(input(f'Digite um Valor para Posição {c}: ')))
    if c == 0:
        mai = men = lista[0]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men :
            men = lista[c]
    
print('-='*30)
print(f'Sua Lista é {lista}')
print(f'O Maior Valoe é {mai} e o Menor Valor é {men}')
