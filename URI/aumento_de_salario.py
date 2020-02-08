def output(salary,grow,percent):
    print('Novo salario: {:.2f}'.format(salary+grow))
    print('Reajuste ganho: {:.2f}'.format(grow))
    print('Em percentual: '+ str(percent) + ' %')

def growCalc(value,percent):
    return value * (percent / 100)


salary = float(input())
newSalary = float
if(salary > 0 and salary <= 400.00):
    newSalary = growCalc(salary,15)
    output(salary,newSalary,15)
if(salary >= 400.01 and salary <= 800.00):
    newSalary = growCalc(salary,12)
    output(salary,newSalary,12)
if(salary >= 800.01 and salary <= 1200.00):
    newSalary = growCalc(salary,10)
    output(salary,newSalary,10)
if(salary >= 1200.01 and salary <= 2000.00):
    newSalary = growCalc(salary,7)
    output(salary,newSalary,7)
if(salary > 2000.00):
    newSalary = growCalc(salary,4)
    output(salary,newSalary,4)