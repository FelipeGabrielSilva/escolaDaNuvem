while True:
  try: 
    num1 = float(input("Informe o valor do primeiro número: "))
    num2 = float(input("Informe o valor do segundo número: "))
    operation = input(
    "Selecione uma operação da calculadora (DIGIE O VALOR DA OPERAÇÃO):" \
    " \n1) SOMA\n2) SUBTRAÇÃO\n3) MULTIPLICAÇÃO\n4) DIVISÃO\n\nOperação: ")

    if operation == "1":
        resultado = num1 + num2
    elif operation == "2":
        resultado = num1 - num2
    elif operation == "3":
        resultado = num1 * num2
    elif operation == "4":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Operação inválida. Divisão por zero.")
            resultado = None
    else:
        raise ValueError("Operação inválida.")

    print(f"Resultado: {resultado}")
    break

  except ZeroDivisionError as e:
    print(f"Erro: {e}")

  except ValueError as e:
    print(f"Erro: {e}: Por favor, tente novamente.")