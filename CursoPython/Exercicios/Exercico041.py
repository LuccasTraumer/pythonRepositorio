''' A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import datetime
now = datetime.now()
print('============ Confederação de Natação ===========================')

nasc = int(input('Digite o Ano de Nascimento: '))
idade = (now.year-nasc)
print(idade)

if idade < 9:
    print('Quem nasceu em {} tem {} anos , '.format(nasc,idade) ,end='')
    print('Portanto está na Categoria: \033[32m MIRIM \033[m')
elif idade > 9 and idade <= 14:
    print('Quem Nasceu em {} tem {} anos e Pertence a Categoria:\033[33m INFANTIL \033[m'.format(nasc,idade))
elif idade > 14 and idade <= 19:
    print('Quem nasceu em {} tem {} anos e Pertence a Categoria: \033[34m JÚNIOR \033[m'.format(nasc,idade))
elif idade > 19 and idade <= 25:
    print('Quem Nasceu em {} tem {} anos e Pertence a Categoria: \033[35m SÊNIOR \033[m'.format(nasc,idade))
else:
    print('Quem nasceu em {} tem {} e Pertence a Categoria: \033[36m MASTER \033[m'.format(nasc,idade))
