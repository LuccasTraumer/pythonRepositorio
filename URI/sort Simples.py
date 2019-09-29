valores = input().split(' ')
primeiroValor = int(valores[0])
segundoValor = int(valores[1])
terceiroValor = int(valores[2])

'''
Se o Primeiro maior
'''
if primeiroValor > segundoValor:
    if primeiroValor > terceiroValor:
        if segundoValor > terceiroValor:
            print(primeiroValor,"\n",segundoValor,"\n",terceiroValor)
        if terceiroValor > segundoValor:
            print(primeiroValor,"\n",terceiroValor,"\n",segundoValor)
''' Segundo Valor Maior'''
if segundoValor > primeiroValor:
    if segundoValor > terceiroValor:
        if primeiroValor > terceiroValor:
            print(segundoValor,"\n",primeiroValor,"\n",terceiroValor)
        if terceiroValor > primeiroValor:
            print(segundoValor,"\n",terceiroValor,"\n",primeiroValor)
''' Terceiro Valor Maior'''
if terceiroValor > primeiroValor:
    if terceiroValor > segundoValor:
        if primeiroValor > segundoValor:
            print(terceiroValor,"\n",primeiroValor,"\n",segundoValor)
        if segundoValor > primeiroValor:
            print(terceiroValor,"\n",segundoValor,"\n",primeiroValor)
print("\n")
print(primeiroValor,"\n",segundoValor,"\n",terceiroValor)
