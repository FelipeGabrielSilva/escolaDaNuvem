import csv

arquivo_csv = "pratica7/data/pessoas.csv"

with open(arquivo_csv, mode="r", encoding="utf-8") as file:
    leitor = csv.DictReader(file)
    print("Dados do arquivo CSV:\n")
    for row in leitor:
        print(f"Nome: {row['Nome']}, Idade: {row['Idade']}, Cidade: {row['Cidade']}")
