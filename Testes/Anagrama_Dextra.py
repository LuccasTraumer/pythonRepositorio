def anagrama(palavra):
    num_pal = len(palavra)
    s = ''
    if num_pal <= 0:
            print("Valor Invalido")
    else:
        for i in range(0,num_pal):
                pal = palavra[i] + palavra[(i+1)],s+palavra[i]
                print(pal)



pal = str(input())

print(anagrama(pal))
