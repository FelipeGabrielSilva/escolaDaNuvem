def calcularDesconto(nomeProduto, precoOriginal, porcentagem):
    desconto = precoOriginal * (porcentagem / 100)
    valorProd = precoOriginal - desconto
    print(
        "O produto", nomeProduto, "tinha o valor original de R$",
          precoOriginal, "com o desconto de R$", desconto,
          "aplicado, o valor final é", valorProd
          )
    

nomeProd = "Camiseta"
precoOrig = 50.00
porcentDesconto = 20

calcularDesconto(nomeProd, precoOrig, porcentDesconto)