def soma_pares(limite) -> int:
    soma = 0
    for i in range(2, limite + 1, 2):
        soma += i
    return soma

def main():
    numero = int(input("Digite um número: "))
    soma = soma_pares(numero)
    print(f"A soma dos números pares até {numero} é de {soma}.")

if __name__ == '__main__':
    main()