import moedas


preco = float(input("Digite o Preco: "))

print("O Dobro de {} é: {}".format(preco,moedas.dobro(preco)))
print("A Metade de {} é: {}".format(preco,moedas.metade(preco)))
print("Aumentando 10% de {} temos: {}".format(preco,moedas.aumentar(preco)))
print("Diminuindo 13% de {} temos: {}".format(preco,moedas.diminuir(preco)))
