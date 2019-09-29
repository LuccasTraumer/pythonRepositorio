def ficha(txt="",gols=""):
    if txt != "" and gols != "":
        return ("O Jogador {} tem {} gols".format(txt,gols))
    if txt != "" and gols == "":
        return ("O Jogador {} tem 0 gols".format(txt))
    if txt == "" and gols != "":
        return ("O Jogador <desconhecido> tem {} gols".format(gols))
    else:
        return ("O Jogador <desconhecido> tem 0 gols")




nome = str(input("Nome do Jogador: "))
marcou = str(input("Quantos gols forammarcados: "))

print(ficha(nome,marcou))