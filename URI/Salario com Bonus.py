nome = str(input())
salario = float(input())
vendas = float(input())
R = vendas*15
Resultado = R/100
aumento = salario+Resultado
print("TOTAL = R$ {:.2f}".format(aumento))
