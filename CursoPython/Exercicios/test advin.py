from random import randint
computador =  randint(0,5)

while True:
    usu = int(input('Digite um Numero: '))
    test = str(input('Quer Continuar?[S/N]: ')).upper()[0]
    if test == 'S':
        test = str(input('Quer Continuar?[S/N]: ')).upper()[0]
        if usu <= 5 :
            if usu == computador:
                print('Voce Venceu')

            else:
                print('Você Perdeu')
        else:
            print('Numero Invalido')
    else:
        print('Fim do Programa')
        break