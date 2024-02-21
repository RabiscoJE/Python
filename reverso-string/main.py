def reverter_string(string) -> str:
    nova_string = ""
    for i in range(len(string) -1 , -1, -1):
        nova_string += string[i]
    return nova_string.capitalize()

def main():
    palavra = input("Digite a palavra a ser invertida: ")
    inversao = reverter_string(palavra)
    print(f"A inversão dessa palavra é '{inversao}'")

if __name__ == '__main__':
    main()
