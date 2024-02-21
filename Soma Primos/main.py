from mmc import primos_ate

def somar_primos(lista) -> int:
    soma = 0
    for n in lista:
        soma += n
    return soma

def main():
    limite = int(input("Digite um número limite: "))
    soma_primos = somar_primos(primos_ate(limite))
    print(f"A soma dos primos até {limite} é igual a {soma_primos}")

if __name__ == "__main__":
    main()