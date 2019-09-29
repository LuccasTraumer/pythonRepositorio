'''
O Sistema que Lista ou Cadastra pessoas em um Arquivo de Texto 
Criar um sistema que vai ter 3 Opções:
1- Listar as Pessoas
2- Cadastrar Pessoas, Nome e Idade
3 - Sair
'''
# Funções 

def listar():
    barra()
    print("           Listar Pessoas           ")
    barra()
    arquivo = open('arquivo.txt','r')
    arquivo.seek(0)
    print(arquivo.read())
    arquivo.close()


def cadastarPessoas():
    barra()
    print('         Cadastro de Pessoas         ')
    barra()
    arquivo = open('arquivo.txt','a')
    nome = str(input('Informe seu Nome: '))
    idade = int(input("Informe sua Idade: "))
    arquivo.append(nome)
    arquivo.append('       ')
    arquivo.append(idade)
    arquivo.append('\n')
    arquivo.close()
    print('Cadastro de {} efetuado com Sucesso!'.format(nome))


def barra():
    print("--------------------------------------------------")


def menu():
    barra()
    print("1- Listar Pessoas ")
    print("2- Cadastra Pessoas ")
    print("3- Sair")
    barra()


try:
    arquivo = open('arquivo.txt','r')
    opcao = 0
    while opcao != 3:
        barra()
        print("          Menu Inicial         ")
        barra()
        menu()
        try:
            opcao = int(input("Informe sua Opção: "))
        except(ValueError,TypeError,KeyboardInterrupt):
            print("Informe uma Opção Valida!")
        if opcao == 1:
            listar()
        if opcao == 2:
            cadastarPessoas()
        if opcao == 3:
            print("Finalizando o Sistema ... ")

except:
    arquivo = open('arquivo.txt','w')
    arquivo.close()
    print("Arquivo foi Criado!")
else:
    print("Executado com Sucesso!")




