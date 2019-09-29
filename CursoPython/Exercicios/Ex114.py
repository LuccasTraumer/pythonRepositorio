import requests

try:
    requests.get("http://www.pudim.com.br")
except:
    print("Não Consegui acessar o Site")
else:
    print("Acesso efetuado com Sucesso!")