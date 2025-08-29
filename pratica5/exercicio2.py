def identificarPalindromo(texto):
    texto = "".join(char.lower() for char in texto if char.isalnum)

    textoOriginal = texto.strip()
    fraseSemEspaco = textoOriginal[::-1].strip()

    if textoOriginal == fraseSemEspaco:
        print("Sim, a frase é um palíndromo")
    else:
        print("Não, a frase não é um palíndromo")

print("\n=== IDENTIFICAR PALÍNDROMO ===")

palindromo = str(input("Digite a frase ou palavra para identificarmos se é um palíndromo: "))
identificarPalindromo(palindromo)