def calcularHorasTrabalhadas(numFunc, horaTrab, valorH):
    res = round(valorH * horaTrab, 2)
    print(
        f"O funcionário {numFunc} trabalhou {horaTrab} horas, "
        f"seu valor hora é R${valorH}. O seu salário é R${res}"
    )
    
numeroFuncionario = int(input("Informe o código do funcionário: "))
horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))
valorHora = float(input("Informe o valor hora do funcionário: R$"))

calcularHorasTrabalhadas(numeroFuncionario, horasTrabalhadas, valorHora)