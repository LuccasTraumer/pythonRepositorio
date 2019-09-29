'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2
e o valor unitário de cada peça 2.
Após, calcule e mostre o valor a ser pago.
'''
#Ler o Codigo, Quantidade de Prod e Preco Produ Unitario
#Valores 1
valores1 = input().split(' ')
qnts1 = int(valores1[1])
preco1 = float(valores1[2])
result1 = qnts1*preco1
# Valores 2
valores2 = input().split(' ')
qnts2 = int(valores2[1])
preco2 = float(valores2[2])
result2 = qnts2*preco2
print("VALOR A PAGAR: {:.2f}".format(result1+result2))
