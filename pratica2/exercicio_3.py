def calcularMediaEscolar(primeiraNota, segundaNota, terceiraNota):
    media = round((primeiraNota + segundaNota + terceiraNota) / 3, 2)
    print("A primeira nota do aluno é", primeiraNota)
    print("A segunda nota do aluno é", segundaNota)
    print("A terceira nota do aluno é", terceiraNota)
    print("O aluno tem a média de ", media)

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

calcularMediaEscolar(nota1, nota2, nota3)