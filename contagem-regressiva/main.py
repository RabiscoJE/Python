import time

def exibir_contagem_regressiva(inicio):
    print("CONTAGEM REGRESSIVA")
    for i in range(inicio, 0, -1):
        print(i)
        time.sleep(1)
    print("Fim!")

def main():
    tamanho = int(input("Digite o tamanho da sua contagem regressiva: "))
    exibir_contagem_regressiva(tamanho)

if __name__ == "__main__":
    main()