try: 
    arquivo = open('arquivo.txt','r')
except:
    arquivo = open('arquivo.txt','w')
else:
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

        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        arquivo.write("Lucas")
        print("Registro de {} adicionado".format(nome))



    def leituraArquivo():
        print("------------------------------------------")
        print("           Pessoas Cadastradas            ")
        print("------------------------------------------")

        print(arquivo.readlines())



    try:
        
        opcao = 0
        while(opcao != 3):
            menu()
            opcao = int(input("Opção Desejada: "))
            if opcao == 1:
                leituraArquivo(arquivo)
            if opcao == 2:
                cadastroPessoa()
    except:
        print("Erro!")
