def exibir_tabuada(numero: int):
    print(10 * "-", f"TABUADA DO {numero}", 10 * "-")
    print()
    for i in range(1, 11):
        print(f"{numero} X {i}  = {numero * i}")

def main():
    numero = int(input("Digite um número: "))
    exibir_tabuada(numero)

if __name__ == "__main__":
    main()