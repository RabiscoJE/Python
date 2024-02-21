def contar_palavras(frase: str) -> int:
    frase.strip()
    return frase.count(" ")

def main():
    frase = input("Digite uma frase: ")
    numero_palavras = contar_palavras(frase)
    print(f"Esta frase tem {numero_palavras} palavras.")

if __name__ == "__main__":
    main()


