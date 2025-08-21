def calcularPrecoTotalCompra(nomeProduto, precoUnitario, quantidade):
    total = precoUnitario * quantidade
    print("O total da compra do produto ", nomeProduto, " é R$", total)

nomeProd = "Cadeira Infantil"
precoUni = 12.40
quant = 3

calcularPrecoTotalCompra(nomeProd, precoUni, quant)