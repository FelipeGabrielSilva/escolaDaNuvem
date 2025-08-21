def calcularComissao(nome, salario, vendas, comissao):
    comis = round(vendas * (comissao / 100), 2)
    total = salario + comis
    print(f"O vendedor {nome} tem o salário fixo de R${salario:.2f}")
    print(f"O vendedor teve um total de vendas de R${vendas:.2f} e tem de {comissao:.2f}%")
    print(f"O valor da sua comissão é R$ {comis:.2f} e seu salário total é R${total:.2f}")
    
nomeFuncionario = input("Informe o primeiro nome do funcionário: ")
salarioFuncionario = float(input("Informe o salário fixo do funcionário: R$"))
totalVendasFuncionario = float(input("Informe o valor total das vendas do funcionário: R$"))
comissaoFuncionario = float(input("Informe a porcentagem da comissão: "))

calcularComissao(nomeFuncionario, salarioFuncionario, totalVendasFuncionario, comissaoFuncionario)