from random import randint, choice
import string

def gerar_senha(tmn: int) -> str:
    senha = ""
    for i in range(0, tmn):
        escolha = randint(0,2)
        novo_caracter = ""
        match escolha:
            case 0:
                novo_caracter = letra_aleatoria()
            case 1:
                novo_caracter = digito_aleatorio()
            case 2:
                novo_caracter = simbolo_aleatorio()
        senha += novo_caracter
    return senha
        

def letra_aleatoria() -> str:
    return choice(string.ascii_letters)

def digito_aleatorio() -> str:
    return choice(string.digits)

def simbolo_aleatorio() -> str:
    return choice(string.punctuation)

def main():
    tamanho = int(input("Digite o tamanho desejado da sua senha: "))
    senha = gerar_senha(tamanho)
    print(senha)

if __name__ == '__main__':
    main()