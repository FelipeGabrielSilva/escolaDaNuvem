while True:
    try:
        print("\n=== CALCULAR MÉDIA DE SALA ===")
        print("Para encerrar o programa, digite 'fim'.")

        notas = []
        nota = ""

        while nota != "fim":
            nota = input("\nInforme o valor da nota: ")

            if nota == "fim":
                break

            valor = float(nota)
            if valor < 0 or valor > 10:
                raise ValueError("Operação inválida. Valor da nota é inválido.")

            notas.append(valor)

        if len(notas) > 0:
            media = sum(notas) / len(notas)
            print(f"\nMédia da sala: {media:.2f}")
        else:
            print("\nNenhuma nota foi informada.")

    except ValueError as e:
        print(f"Erro: {e} Por favor, tente novamente.")
