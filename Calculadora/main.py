def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        print('Erro: Divisão por zero.')

def menu():
    print(20 * '-')
    print('MENU')
    print(20 * '-')
    print('[1] Adição')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão')

def get_escolha():
    while True:
        escolha = int(input('Digite Sua escolha?'))

        if 4 >= escolha >= 0:
            return escolha
        else:
            print('escolha invalida!')

def continuar():
    while True:
        print()
        continuar = input('Quer continuar? [s], [n]')
        if continuar.lower() == 's':
            return True
        elif continuar.lower() == 'n':
            return False
        else:
            print('Resposta invalida')

def exibir_resultado(operacao, a, b, resultado):
    print(f'A {operacao} de {a} e {b} resulta em {resultado}')

def main():
    while True:
        menu()
        escolha = get_escolha()
        num_1 = int(input('Digite o primeiro número: '))
        num_2 = int(input('Digite o segundo número: '))

        if escolha == 1:
            resultado = adicao(num_1, num_2)
            
        elif escolha == 2:
            resultado = subtracao(num_1, num_2)
            exibir_resultado('adicao', num_1, num_2, resultado)
        elif escolha == 3:
            resultado = multiplicacao(num_1, num_2)
            print(f'A multiplicação de {num_1} por {num_2} resulta em {resultado}')
        elif escolha == 4:
            resultado = divisao(num_1, num_2)
            print(f'A divisão de {num_1} por {num_2} resulta em {resultado}')
        
        if not continuar():
            print("Até mais!")
            break

if __name__ == '__main__':
    main()