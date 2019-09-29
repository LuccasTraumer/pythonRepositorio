'''
O arquivo de entrada contém dois valores inteiros correspondentes ao
código e à quantidade de um item conforme tabela acima.
'''
valores = input().split(' ')
cod = int(valores[0])
qtd =  int(valores[1])

if cod == 1:
    print("Total: R$ {:.2f}".format(qtd * 4.0))
if cod == 2:
    print("Total: R$ {:.2f}".format(qtd*4.5))
if cod == 3:
    print("Total: R$ {:.2f}".format(qtd*5.0))
if cod == 4:
    print("Total: R$ {:.2f}".format(qtd*2.0))
if cod == 5:
    print("Total: R$ {:.2f}".format(qtd*1.5))
