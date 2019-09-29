def maior(*valores):
    maio = 0
    for num in valores:
        if num > maio:
            maio = num
    print("O Maior valore é {:.0f}".format(maio))
    print("A Quantidade de Numeros Informados são: {:.0f}".format(len(valores)))

maior(5, 4 ,1 , 2)
