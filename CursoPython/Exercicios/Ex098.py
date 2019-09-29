def contador(inicio,fim,passo):
    if inicio < fim:
        while inicio <= fim:
            inicio += passo
            print(inicio)
    if inicio > fim:
        while inicio > fim:
            inicio -= passo
            print(inicio)


contador(10,0,2)
