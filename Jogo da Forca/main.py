import random

def sortear_palavra(lista: list) -> str:
    numero_aleatorio = random.randint(0, len(lista) - 1)
    return lista[numero_aleatorio][1]

def exibir_campos(palavra, tema, vida) -> None:
    print(palavra)
    print(tema)
    print(vida)
    print()

def is_letra_in_palavra(letra, palavra) -> bool:
    if letra in palavra:
        return True
    else:
        return False

def get_letras_atualizadas(letra, palavra, letras) -> None:
    nova_palavra = ""
    for i, l in enumerate(palavra):
        if l == letra:
            nova_palavra += l
        else:
            nova_palavra += letras[i]
    return nova_palavra



def main():
    palavras_secretas = [
        ["fruta", "graviola"],
        ["animal", "abelha"],
        ["profissão", "professor"]
    ]
    vida = 5
    numero_aleatorio = random.randint(0, len(palavras_secretas) - 1)
    palavra_escolhida = palavras_secretas[numero_aleatorio][1]
    tema = palavras_secretas[numero_aleatorio][0]
    letras_reveladas = len(palavra_escolhida) * "*"

    while vida > 0:
        exibir_campos(letras_reveladas, tema, vida)
        palpite = input("Escolha uma letra: ").lower()[0]

        if is_letra_in_palavra(palpite, palavra_escolhida):
            letras_reveladas = get_letras_atualizadas(palpite, palavra_escolhida, letras_reveladas)
            print("Há essa letra na palavra")
            if letras_reveladas == palavra_escolhida:
                exibir_campos(letras_reveladas, tema, vida)
                print("Parabens você acertou!")
                break
        else:
            vida -= 1
            print("Não há essa letra. Você perdeu uma vida!")
    print("Fim de jogo")


if __name__ == "__main__":
    main()