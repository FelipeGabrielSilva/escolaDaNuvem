import requests

def consultarCEP(cep):
    if len(str(cep)) != 8:
        print("O CEP informado é inválido")
        return

    base_url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(base_url).json()
    
    if "erro" in response:
        print("CEP não encontrado!")
    else:
        print("\n=== Resultado da consulta ===")
        print(f"CEP: {response['cep']}")
        print(f"Logradouro: {response['logradouro']}")
        print(f"Bairro: {response['bairro']}")
        print(f"Cidade: {response['localidade']}")
        print(f"Estado: {response['uf']}")


cep = int(input("Informe o CEP a ser consultado (APENAS NÚMEROS): "))
consultarCEP(cep=cep)