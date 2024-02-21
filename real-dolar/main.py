def real_para_dolar(valor) -> float:
    valor_dolar = valor / 5
    return valor_dolar

def main():
    valor = int(input("Qual valor você quer converter para dolares? R$"))
    valor_dolar = real_para_dolar(valor)
    print(f"R${valor:.2f} são equivalentes a US${valor_dolar:.2f}.")


if __name__ == "__main__":
    main()