from datetime import date
peg = date.today()
AnoA = peg.year
def voto(anoInf):
    global AnoA
    idade = AnoA - anoInf
    if idade < 16:
        return ("Com {} anos: VOTO é Negado".format(idade))
    if idade > 16 and idade < 18 or idade > 65:
        return ("Com {} anos: VOTO é Opcional".format(idade))
    if idade > 18 and idade < 65:
        return ('Com {} anos: VOTO é Obrigatorio'.format(idade))


AnoNas = int(input("Informe o Ano de Nascimento: "))

print(voto(AnoNas))