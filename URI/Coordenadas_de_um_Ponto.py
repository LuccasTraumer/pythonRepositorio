valores = input().split(' ')
x = float(valores[0])
y = float(valores[1])

if x == 0 and y == 0:
    print("Origem")
if x > 0 and y > 0:
    print("Q1")
if x > 0 and y < 0:
    print("Q4")
if x < 0 and y > 0:
    print("Q2")
if x < 0 and y <0:
    print("Q3")
if x > 0 and y ==0:
    print("Eixo X")
if y>0 and x == 0:
    print("Eixo Y")