contPosi = 0
contNega = 0
contImpar = 0
contPar = 0
for i in range(0,5):
    value = float(input())
    if(value % 2 == 0):
        contPar = contPar + 1
    else:
        contImpar = contImpar + 1
    if(value >= 0):
        contPosi = contPosi + 1
    else:
        contNega = contNega + 1

print(str(contPar) + ' valor(es) par(es)')
print(str(contImpar) + ' valor(es) impar(es)')
print(str(contPosi) + ' valor(es) pasitivo(s)')
print(str(contNega) + ' valor(es) negativo(s)')