def calcularMediaEscolaPonderada(pNota, sNota, tNota, qNota):
    media = ((pNota * 2) + (sNota * 3) + (tNota * 4) + (qNota * 1)) / 10
    print(f"Média: {media:.1f}")
    
    if (media >= 7):
        print("Aluno aprovado")
    elif (media < 5):
        print("Aluno reprovado")
    elif (media >= 5 and media <= 6.9):
        print("Aluno em exame\n\n")
        alunoEmExame(media)
        
        
def alunoEmExame(mediaAluno):
    notaExame = float(input("Informe a nota do exame: "))
    print(f"\n\n\nNota do exame: {notaExame}")
    mediaAluno = (mediaAluno + notaExame) / 2
    
    if (mediaAluno > 4.9):
        print("Aluno aprovado")
    elif (mediaAluno < 5):
        print("Aluno reprovado")
        
    print(f"A média do aluno é {mediaAluno:.1f}")
    


N1 = float(input("Informe o valor da nota 1: "))
N2 = float(input("Informe o valor da nota 2: "))
N3 = float(input("Informe o valor da nota 3: "))
N4 = float(input("Informe o valor da nota 4: "))

calcularMediaEscolaPonderada(N1, N2, N3, N4)