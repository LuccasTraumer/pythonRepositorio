'''
Crie um Pequeno sistema modularizado que permite cadastrar pessoas pelo seu
Nome e Idade em Arquivo de texto simples.
O Sistema vai ter 3 opções:
1: Cadastra uma Pessoa,
2: Listar todas as Pessoas
3: Sair
'''
def menu():
        print("------------------------------------------")
        print("              Menu Principal              ")
        print("------------------------------------------")
        print("1-  Ver Pessoas Cadastradas")
        print("2-  Cadastra Nova Pessoa")
        print("3-  Sair")

def cadastroPessoa():
    print("------------------------------------------")
    print("              Novo Cadastro               ")
    print("------------------------------------------")
    arquivo = open('arquivo.txt','a')
    try:
        try:
            nome = str(input("Nome: "))
        except(KeyboardInterrupt,ValueError):
            print("Parou o Software ou deixou de digitar")
        else:
            arquivo.write(nome)
        try:
            idade = int(input("Idade: "))
        except(ValueError,TypeError,KeyboardInterrupt):
            print("Valor Invalido!")
        else:
            arquivo.write('          ')
            arquivo.write(str(idade))
            arquivo.write(' Anos')
            arquivo.write('\n')
            arquivo.close()
            print("{} Cadastrada com Sucesso!".format(nome))
    except:
        print("Erro nos Valores Informados !")


def leituraArquivo():
    print("------------------------------------------")
    print("           Pessoas Cadastradas            ")
    print("------------------------------------------")
    arquivo = open('arquivo.txt','r')
    arquivo.seek(0)
    print(arquivo.read())
    arquivo.close()


try:
    arquivo = open('arquivo.txt','r')
except:
    arquivo = open('arquivo.txt','w')
    print("Arquivo Criado com Sucesso!")
else:
    opcao = 0
    while(opcao != 3):
        menu()
        try:
            opcao = int(input("Opção Desejada: "))
        except(ValueError,TypeError,KeyboardInterrupt):
            print("Valor Invalido")
        else:
            if opcao == 1:
                leituraArquivo()
            if opcao == 2:
                cadastroPessoa()
            if opcao == 3:
                print("Finalizando o Sistema ")





