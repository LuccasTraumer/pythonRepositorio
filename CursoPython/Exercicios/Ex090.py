'''
Faca um Programa que leia Nome e  Media de um aluno, guradando tambem a situação em um dicionario.
No Final, Mostre o conteudo da estrutura na tela
Média 7+ aprovado, 7 pra baixo Reprovado
'''
aluno = {}
aluno['Nome'] = str(input('Nome do Aluno: '))
aluno['Media']= float(input('Média do Aluno: '))
if aluno['Media']<= 7:
    print(f'O Aluno {aluno["Nome"]}')
    print(f'Média é Igual {aluno["Media"]}')
    print('Situação é Igual a: Reprovado')
else:
    print(f'O Aluno {aluno["Nome"]}')
    print(f'Media igual {aluno["Media"]}')
    print('Situação é Igual a: Aprovado')

