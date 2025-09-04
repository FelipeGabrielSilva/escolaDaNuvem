import requests
from datetime import datetime

def consultarMoeda(moeda):
    base_url = f"https://economia.awesomeapi.com.br/json/last/{moeda.upper()}-BRL"
    resp = requests.get(base_url)
    if resp.status_code != 200:
        print("Erro ao acessar a API.")
        return

    data = resp.json()
    key = f"{moeda.upper()}BRL"
    if key not in data:
        print("Código de moeda inválido ou não encontrado.")
        return

    info = data[key]
    bid = info["bid"]
    high = info["high"]
    low = info["low"]
    timestamp = int(info["timestamp"])
    create_date = info["create_date"]

    dt = datetime.fromtimestamp(timestamp)

    print("\n=== Cotação Atual ===")
    print(f"Moeda: {info['name']}")
    print(f"Valor atual (bid): R$ {bid}")
    print(f"Máximo do dia: R$ {high}")
    print(f"Mínimo do dia: R$ {low}")
    print(f"Data/hora (serve timestamp): {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Data/hora (create_date): {create_date}")

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip()
consultarMoeda(moeda)