def converterMoeda(primeiraMoeda, segundaMoeada):
    res = round(primeiraMoeda / segundaMoeada, 2)
    print("O resultado da conversão é", res)

reais = 100.00
dolar = 5.60
euro = 6.60

converterMoeda(reais, dolar)
converterMoeda(reais, euro)