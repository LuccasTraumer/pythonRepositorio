# Esquerda Menor Subtrai
# Esquerda Maior Soma

linha1 = input().split(' ')
numEsq1 = int(linha1[0])
numDir1 = int(linha1[1])
linha2 = input().split(' ')
numEsq2 = int(linha2[0])
numDir2 = int(linha2[1])

if numEsq1 >= numDir1:
    print(abs(numEsq1 + numDir1))
if numEsq1 < numDir1:
    print(abs(numEsq1 - numDir1))
if numEsq2 < numDir2:
    print(abs(numEsq2 + numDir2))
if numEsq2 >= numDir2:
    print(abs(numEsq2 - numDir2))