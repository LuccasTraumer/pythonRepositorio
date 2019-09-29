'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, 
o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e 
o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
'''

linha1 = input().split(' ')
linha2 = input().split(' ')

#Linha 1
codPeca1 = int(linha1[0])
qtsPecas1 = int(linha1[1])
precoUnitario1 = float(linha1[2])
soma1 = qtsPecas1 * precoUnitario1
#Linha 2 
codPeca2 = int(linha2[0])
qtsPecas2 = int(linha2[1])
precoUnitario2 = float(linha2[2])
soma2 = qtsPecas2*precoUnitario2
#Soma
soma = soma1+soma2
print("VALOR A PAGAR: R$ {:.2f}".format(soma))