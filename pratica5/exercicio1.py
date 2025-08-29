def calcularValorGorjeta(conta, gorjeta):
    valor = conta * (gorjeta / 100)
    print(f"\nO valor da gorjeta: R${valor:.2f}")

valorConta = float(input("Informe o valor da conta: R$"))
porcentagem = int(input("Informe o valor da gorjeta (NÚMERO INTEIRO): "))

calcularValorGorjeta(valorConta, porcentagem)