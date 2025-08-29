while True:
    try:
        print("\n=== CONTADOR DE NÚMEROS ÍMPARES E PARES ===")
        print("Para encerrar o programa, digite 'fim'.")

        pares = []
        impares = []
        numero = ""

        while numero != "fim":
            numero = input("\nInforme o valor do número: ")

            if numero == "fim":
                break

            valor = int(numero)

            if valor % 2 == 0:
                print("O número informado é par")
                pares.append(valor)
            else:
                print("O número informado é ímpar")
                impares.append(valor)
                
        print(f"A quantidade de números pares são: {len(pares)}")
        print(f"A quantidade de números ímpares são: {len(impares)}")

    except ValueError as e:
        print(f"Erro: {e} Por favor, tente novamente.")
