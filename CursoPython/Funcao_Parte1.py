'''
def soma(a,b):
    s = a+b
    print(s)


a = int(input())
b = int(input())
soma(a,b)


valores = [7,4,5,6,2]

def dobra(lst):
    pos = 0
    while pos < len(lst):
        print(lst[pos]*2)
        pos +=1


dobra(valores)
'''
def soma(*valores):
    s = 0
    for num in valores:
        s+= num
    print(s)


soma(5,4)
soma(10,5,4,3,8)
