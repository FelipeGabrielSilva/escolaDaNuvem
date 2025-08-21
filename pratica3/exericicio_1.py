def calcularAreaCircuferencia(pi, raio):
    res = round(pi * pow(raio, 2), 4)
    print(f"A = {res}")

raio = float(input("Informe o raio da circuferência: "))
pi = 3.14159265

calcularAreaCircuferencia(pi, raio)