import random, os, string

def gerarSenhaAleatoria(qtd):
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed(os.urandom(1024))
    senha = ''.join(random.choice(chars) for i in range(qtd))

    print(f"SENHA GERADA: {senha}")

quantidade = int(input("Informe o tamanho da senha a ser gerada: "))
gerarSenhaAleatoria(quantidade)