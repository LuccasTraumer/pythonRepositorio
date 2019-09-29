try:
    a = int(input("Numerador: "))
    b =  int(input("Denominador: "))
    r = a/b
except ZeroDivisionError:
    print("Não é possivel dividir um Numero por 0!")
except (ValueError,TypeError):
    print("Tivemos um Problema no Tipo de dados que você digitou ")


else:
    print("O resultado é: {:.1f}".format(r))
finally:
    print("Volte Sempre !")