def calculadoraIMC(peso, altura):
    imc = round(peso / (altura * altura),2)
    print(imc)
    
    if (imc < 18.5):
        print("Abaixo do peso")
    elif (imc < 25):
        print("Peso normal")
    elif (imc < 30):
        print("Sobrepreso")
    else:
        print("Obeso")

pesoInfo = float(input("Informe o peso em KG: "))
alturaInfo = float(input("Informe a altura em metros: "))

calculadoraIMC(pesoInfo, alturaInfo)