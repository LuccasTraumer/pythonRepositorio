'''
Cod       Produto        Preco
1     Cachorro Quente     4.00
2     X-Salada            4.50
3     X-Bacon             5.00
4     Torrada Simples     2.00
5     Refrigerante        1.50
'''

informacoes = input().split(' ')
codigo = int(informacoes[0])
qts = int(informacoes[1])

if codigo == 1:
    print("Total: R$ {:.2f}".format(qts*4.00))
if codigo == 2:
    print("Total: R$ {:.2f} ".format(4.50 * qts))
if codigo == 3:
    print("Total: R$ {:.2f}".format(5.00*qts))
if codigo == 4:
    print("Total: R$ {:.2f}".format(2.00*qts))
if codigo == 5:
    print("Total: R$ {:.2f}".format(1.50*qts))
