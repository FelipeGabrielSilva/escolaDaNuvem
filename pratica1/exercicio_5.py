def calcularDiferenca(
        primeiroNumero,
        segundoNumero,
        terceiroNumero,
        quartoNumero
        ):
    res = (primeiroNumero * segundoNumero - terceiroNumero * quartoNumero)
    print("DIFERENCA =", res)

a = int(input("Informe o valor do primeiro número: "))
b = int(input("Informe o valor do segundo número: "))
c = int(input("Informe o valor do terceiro número: "))
d = int(input("Informe o valor do quarto número: "))

calcularDiferenca(a, b, c, d)