def conversorTemperatura(temp, orig, dest):
    res = None
    
    if orig == "C" and dest == "F":
        res = temp * 1.8 + 32
    elif orig == "C" and dest == "K":
        res = temp + 273.15
    elif orig == "F" and dest == "C":
        res = (temp - 32) / 1.8
    elif orig == "F" and dest == "K":
        res = (temp - 32) * 5/9 + 273.15
    elif orig == "K" and dest == "C":
        res = temp - 273.15
    elif orig == "K" and dest == "F":
        res = (temp - 273.15) * 9/5 + 32
    else:
        print("Conversão inválida!")
        return
    
    print(f"A temperatura de {temp}{orig} para {dest} é: {res:.2f}{dest}")


origem = input("Informe a origem da temperatura (C para celsius, K para kelvin, F para Fahrenhrit): ").upper()
temperatura = float(input("Informe a temperatura: "))
destino = input("Informe para qual unidade você quer converter (C para celsius, K para kelvin, F para Fahrenhrit): ")

conversorTemperatura(temperatura, origem, destino)