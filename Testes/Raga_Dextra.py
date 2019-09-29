'''
def Frases(fras1,frase2):
    num_fras1 = len(fras1)
    num_fras2 = len(frase2)
    whis = False
    if num_fras1 < num_fras2:
        for i in range(0,num_fras1,1):
            letra = frase2[i]
            if letra in frase1:
                whis = True
    if num_fras1 > num_fras2:
        for i in range(0,num_fras2,1):
            letra = frase2[i]
            if letra in frase1:
                whis = True
        

    return whis



frase1 = str(input()).lower().replace(" ","")
frase2 = str(input()).lower().replace(" ","")

print(Frases(frase1,frase2))
'''
def permuta(s,s1 = ''):
    if len(s) == 0:
        print (s1)
    else:
        tam_s = len(s)
        for i in range(0,tam_s):
            print(permuta(s[i]+s[(i+1)],s1+s[i]))
            

palavra = str(input())

print(permuta(palavra))
