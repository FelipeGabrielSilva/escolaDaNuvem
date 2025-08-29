import re

while True:
    try:
        print("\n=== SENHA FORTE ===")
        print("O usuário deve informar um senha com minímo de 8 caracteres e deve conter um número")

        senha = str(input("\nInforme a senha: "))
        numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        if len(senha) < 8:
            raise ValueError("A senha não atende o requisito de tamanho.")
        
        if not any(char.isdigit() for char in senha):
            raise ValueError("A senha não atende o requisito de conter pelo menos um número.")

        print("\nSenha válida")
        break

            

    
    except ValueError as e:
        print(f"Erro: {e}")