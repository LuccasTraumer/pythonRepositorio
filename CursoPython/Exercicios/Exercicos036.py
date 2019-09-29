'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('--------------------\033[35m Emprestimo de Casa \033[m ------------------------------------')

casa = float(input('Digite o Valor da Casa: '))
#valor_ca.strip()
salario = float(input('Digite o seu Salário: '))
#salario.strip()
parcelas = int(input('Digite em Quantos anos voce vai pagar a Casa: '))
#parcelas.strip()

meses = casa/(parcelas*12)

mens = (salario*30/100)

if meses <= mens:
    print('Emprestimo \033[33m CONCEDIDO \033[m')
else:
    print('Emprestimo \033[31m NEGADO \033[m')
print('Para pagar um casa de {:.2f} em {} Anos'.format(casa,parcelas), end='')
print('a Prestação será de {:.2f}'.format(meses))


