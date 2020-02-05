'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário 	Percentual de Reajuste

0 - 400.00               15%
400.01 - 800.00          12%
800.01 - 1200.00         10%
1200.01 - 2000.00        7%
Acima de 2000.00         4%

'''

def view(salary,grow,perc):
    print('Novo salario: {:.2f}'.format(salary))
    print('Reajuste ganho: {:.2f}'.format(grow))
    print('Em percentual: '+ str(perc) + ' %')


salary = float(input())

if(salary > 0 and salary <= 400.00):
    grow = salary * 0.15
    view(salary+grow,grow,15)
if(salary > 400.01 and salary <= 800.00):
    grow = salary*0.12
    view(salary+grow, grow, 12)
if(salary > 800.01 and salary <= 1200.00):
    grow = salary * 0.10
    view(salary+grow, grow, 10)
if(salary > 1200.01 and salary <= 2000.00):
    grow = salary * 0.07
    view(salary + grow, grow, 7)
if(salary > 2000.00):
    grow = salary * 0.04
    view(salary+grow, grow, 4)