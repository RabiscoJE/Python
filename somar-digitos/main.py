def somar_digitos(numero: str):
    soma = 0
    for digito in numero:
        soma += int(digito)
    return soma

def main():
    numero = input("Digite um número: ")
    soma = somar_digitos(numero)
    print(f"A soma dos algarismos de {numero} é {soma}.")

if __name__ == "__main__":
    main()