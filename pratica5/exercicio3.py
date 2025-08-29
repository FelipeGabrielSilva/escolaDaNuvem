def valorFinalDoProdutoComDesconto(valor, desconto):
    desc = valor * (desconto / 100)
    valorProduto = valor - desc

    print(f"O valor do produto é R${valorProduto:.2f}")
    print(f"O valor do desconto é R${desc:.2f}")

print("\n=== CALCULAR PREÇO FINAL DE UM PRODUTO COM DESCONTO ===\n")
preco = float(input("Informe o valor do produto (Utilize . para casa decimal): R$"))
porcentagem = int(input("Informe o valor do desconto (NÚMERO INTEIRO): "))

valorFinalDoProdutoComDesconto(preco, porcentagem)