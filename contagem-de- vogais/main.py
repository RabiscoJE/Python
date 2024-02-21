def get_num_vogais(txt: str) -> int:
    vogais = "aeiou"
    num_vogais = 0
    for l in vogais:
        num_vogais += txt.count(l)
    return num_vogais

def main():
    palavra = input("Digite uma palavra qualquer: ")
    num_vogais = get_num_vogais(palavra)
    print(f"Essa palavra tem {num_vogais} vogais")

if __name__ == '__main__':
    main()