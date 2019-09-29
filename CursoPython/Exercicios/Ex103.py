def leiaint(dig):

    if type(dig) == int:
        return ("O Valor {} é um Inteiro.".format(dig))
    else:
        return ("[ERRO] Informe um valor Valido!")


num = int(input("Informe: "))
print(leiaint(num))