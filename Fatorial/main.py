def fatorial(num: int):
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        return 'Inexistente'
    else:
        return fatorial(num -1) * num


def main():
    numero = int(input('Digite um número: '))
    print(f'O fatorial de {numero} é {fatorial(numero)}.')

if __name__ == '__main__':
    main()