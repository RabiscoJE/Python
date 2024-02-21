def sequencia_fibonati(limite: int):
    sequencia = []
    for i in range(1, limite + 1):
        sequencia.append(fibonacci(i))
    return sequencia

def fibonacci(numero: int):
    if numero < 2:
        return numero
    return fibonacci(numero - 1) + fibonacci(numero - 2)

def main():
    limite = int(input("Digite até qual número da sequência você quer ver: "))
    sequencia = sequencia_fibonati(limite)
    print(sequencia)

if __name__ == '__main__':
    main()