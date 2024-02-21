import reverso

def is_palindromo(frase) -> bool:
    frase_invertida = reverso.reverter_string(frase)
    if frase == frase_invertida:
        return True
    else:
        return False

def main():
    texto = input("digite uma palavra ou frase: ").replace(" ", "").lower()
    resultado = is_palindromo(texto)
    if resultado == True:
        print("O texto digitado é um palindromo!")
    else:
        print("O texto digitado não é um palindromo!")

if __name__ == "__main__":
    main()