import json

arquivo_json = "pratica7/data/pessoa.json"

pessoas = [
    {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 34, "cidade": "Rio de Janeiro"},
    {"nome": "Carla", "idade": 25, "cidade": "Belo Horizonte"},
    {"nome": "Diego", "idade": 30, "cidade": "Curitiba"},
    {"nome": "Mariana", "idade": 22, "cidade": "Porto Alegre"},
    {"nome": "Felipe", "idade": 40, "cidade": "Recife"},
    {"nome": "Juliana", "idade": 27, "cidade": "Fortaleza"},
    {"nome": "Ricardo", "idade": 31, "cidade": "Salvador"},
    {"nome": "Paula", "idade": 29, "cidade": "Florianópolis"},
    {"nome": "Lucas", "idade": 35, "cidade": "Campinas"},
    {"nome": "Fernanda", "idade": 26, "cidade": "Natal"},
    {"nome": "Gustavo", "idade": 33, "cidade": "Manaus"},
    {"nome": "Isabela", "idade": 24, "cidade": "Belém"},
    {"nome": "Rafael", "idade": 38, "cidade": "Goiânia"},
    {"nome": "Camila", "idade": 21, "cidade": "Vitória"},
    {"nome": "André", "idade": 32, "cidade": "João Pessoa"},
    {"nome": "Letícia", "idade": 23, "cidade": "Maceió"},
    {"nome": "Thiago", "idade": 36, "cidade": "São Luís"},
    {"nome": "Patrícia", "idade": 28, "cidade": "Teresina"},
    {"nome": "Eduardo", "idade": 39, "cidade": "Aracaju"}
]

with open(arquivo_json, mode="w", encoding="utf-8") as file:
    json.dump(pessoas, file, ensure_ascii=False, indent=4)

print(f"Arquivo '{arquivo_json}' criado com sucesso!")

with open(arquivo_json, mode="r", encoding="utf-8") as file:
    dados = json.load(file)
    print("\nDados do arquivo JSON:")
    for dados in pessoas:
        print(f"Nome: {dados['nome']}, Idade: {dados['idade']}, Cidade: {dados['cidade']}")