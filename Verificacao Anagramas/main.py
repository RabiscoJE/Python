def is_anagramas(palavra_1, palavra_2) -> bool:
    if len(palavra_1) != len(palavra_2):
        return False
    for l in palavra_1:
        if l not in palavra_2:
            return False
    return True

def main():
    p1 = input("Digite a primeira palavra: ").lower()
    p2 = input("Digite a segunda palavra: ").lower()
    if is_anagramas(p1, p2):
        print(f"{p1} e {p2} são anagramas!")
    else:
        print(f"{p1} e {p2} NÃO são anagramas!")

if __name__ == "__main__":
    main()