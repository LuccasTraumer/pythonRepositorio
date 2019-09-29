def Area(larg,compr):
    print(f'A área de um terreno {larg}x{compr} é de {larg*compr}m')


print("  Controle de Terreno")
print("------------------------")
larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))

Area(larg,comp)
