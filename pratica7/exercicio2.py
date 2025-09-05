import csv

arquivo_csv = "pratica7/data/pessoas.csv"

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 28, "São Paulo"],
    ["Bruno", 34, "Rio de Janeiro"],
    ["Carla", 25, "Belo Horizonte"],
    ["Diego", 30, "Curitiba"],
    ["Mariana", 22, "Porto Alegre"]
]

with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(dados)

print(f"Arquivo '{arquivo_csv}' criado com sucesso!")
