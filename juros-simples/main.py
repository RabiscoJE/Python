def juros_simples(principal, taxa, tempo) -> float:
    juro = (principal * (taxa / 100)) * tempo
    return juro

def main():
    valor = float(input("Valor do principal: R$"))
    taxa = float(input("Taxa aplicada: %"))
    tempo = float(input("Tempo em mêses: "))
    juro = juros_simples(valor, taxa, tempo)
    montante = valor + juro
    print(f'''Um empréstimo no valor de R${valor:.2f}, com uma taxa de {taxa:.0f}%
gerará um valor de R${juro:.2f} em juros, 
resultando em um montante de R${montante:.2f}''')

if __name__ == "__main__":
    main()