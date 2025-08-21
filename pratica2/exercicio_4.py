def calcularConsumoMedioDeCombustivel(dist, combGasto):
    res = round(dist / combGasto, 2)
    print(
        "A distância percorrida é", dist,
        "km com", combGasto, "km/l de combustível gasto",
        ", a média de gasto na viagem foi", res
          )
    
distancia = 783
combustivelGasto = 25

calcularConsumoMedioDeCombustivel(distancia, combustivelGasto)