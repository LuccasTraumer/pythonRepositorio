'''
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal,
correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1, respectivamente,
para cada uma destas notas e mostre esta média acompanhada pela mensagem
"Media: ". Se esta média for maior ou igual a 7.0,
imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0,
imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9,
inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame,
leia um valor correspondente à nota do exame obtida pelo aluno.
Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2).
e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou
"Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos).
Para estes dois casos (aprovado ou reprovado após ter pego exame)
apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.
'''
exame = 0
valores = input().split(' ')
for i in valores:
    if i == 4:
        exame = float(valores[4])
n1 = float(valores[0]) #Peso 2 (n1*2)
n2 = float(valores[1]) #Peso 3 (n2*3)
n3 = float(valores[2]) # Peso 4 (n3*4)
n4 = float(valores[3]) # Peso 1 (n4*1)


media = float((n1*2) + (n2*3) + (n3*4) + (n4*1)/4)
print(media)
'''
if media < 5:
    print("Aluno reprovado")
    print("Media final: {:.1f}".format(media))
if media >= 5 and media <= 6.9:
    print("Aluno em exame")
    print("Nota do Exame: {:.1f}".format(exame))
    mediaE = (media + exame)/2
    if mediaE >= 5:
        print("Aluno aprovado")
        print("Media final: {:.1f}".format(mediaE))
    else:
        print("Aluno reprovado")
        print("Media final: {:.1f}".format(mediaE))
    
if media >= 7:
    print("Aluno aprovado")
    print("Media: {:.1f}".format(media))
'''
