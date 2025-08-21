def classificacaoIdade(idade):
    if (idade < 13) :
        print("O usuário é classificado como criança")
    elif (idade < 18) :
        print("O usuário é classificado como adolescente")
    elif (idade < 60) :
        print("O usuário é classificado como adulto")
    else :
        print("O usuário é classificado como idoso")
    
idadeInfo = int(input("Informe a idade: "))

classificacaoIdade(idadeInfo)