qtsAlunos = int(input("Quantos Alunos: "))
alunos = []

def media(n1=0,n2=0,n3=0,n4=0):
    return (n1+n2+n3+n4)/4


def aprovado(medi):
    aprov = False
    if medi >= 8.0:
        aprov = True
    return aprov



def medGeral(notas,qtsAlunos):
    sumNota = 0
    sumNota += notas
    return sumNotas/qtsAlunos

def maiorNota(media):
    maiorNota = 0
    if media > maiorNota:
        maiorNota = media
    return maiorNota
    
def contAprova(aprov):
    cnt = 0
    if aprov == True:
        cnt +=1
    return cnt

for i in range(0,qtsAlunos,1):
    nota1 = float(input("Primeira Nota: "))
    nota2 = float(input("Segunda Nota: "))
    nota3 = float(input("Terceira Nota: "))
    nota4 = float(input("Quarta Nota: "))
    medi = media(nota1,nota2,nota3,nota4)
    aprova = aprovado(medi)
    medGer = medGeral(medi,qtsAlunos)
    maiorNo = maiorNota(medi)
    qtsAprov = contAprova(aprova)
    alunos.append(medi,aprova,medGer,maiorNo,qtsAprov)
    
    
print("O Aluno teve {:.2f} e foi {}")
print("O Aluno teve {:.2f} e foi {}")
print("O Aluno teve {:.2f} e foi {}")
print("O Aluno teve {:.2ff} e foi {}")
print("Alunos Aprovados: {}")
print("Média da Turma: {}")
print("Maior Media Obtida: {}")
    
