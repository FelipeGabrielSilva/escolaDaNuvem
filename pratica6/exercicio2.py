import requests

def getRandomUsers(qtd):
    base_url = f"https://randomuser.me/api/?results={qtd}"
    response = requests.get(base_url).json()
    return response["results"]  # acessa apenas a lista de usuários

def filtrarInformacoes(users):
    filtrado = [
        {
            "nome": f'{u["name"]["first"]} {u["name"]["last"]}',
            "email": u["email"],
            "pais": u["location"]["country"]
        }
        for u in users
    ]
    return filtrado

def exibirUsuarios(qtd):
    users = getRandomUsers(qtd)
    users = filtrarInformacoes(users)

    print("\n===USUÁRIO GERADOS===")
    for i, u in enumerate(users, start=1):
        print(f"{i}. {u['nome']} | {u['email']} | {u['pais']}")

quantidade = int(input("Informe a quantidade de usuários a serem criados: "))
exibirUsuarios(quantidade)
