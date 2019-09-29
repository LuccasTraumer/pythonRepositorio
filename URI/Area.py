'''
a) a área do triângulo retângulo que tem A por base e C por altura. 
b) a área do círculo de raio C. (pi = 3.14159) 
c) a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado que tem lado B. 
e) a área do retângulo que tem lados A e B. 
'''
valores = input().split(' ')
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
pi = 3.14159
# Area = b*h/2
area = A*C/2
# A = pi * r**2
A_Circulo = pi * C**2
# A = B+b*h/2
A_Trapezio = (A+B)*C/2
# Area_Quadrado A= b*b
A_Quadrado = B*B
# Area Retangulo A= b*h
A_Retangulo = A*B


print("TRIANGULO: {:.3f}".format(area))
print("CIRCULO: {:.3f}".format(A_Circulo))
print("TRAPEZIO: {:.3f}".format(A_Trapezio))
print("QUADRADO: {:.3f}".format(A_Quadrado))
print("RETANGULO: {:.3f}".format(A_Retangulo))
