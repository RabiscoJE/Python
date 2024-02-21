def get_valor_maximo(lista: list):
    return max(lista)

def get_valor_minimo(lista):
    return min(lista)

def get_valor_maximo2(lista):
    maximo = None
    for v in lista:
        if maximo == None:
            maximo = v
        elif v > maximo:
            maximo = v
    return maximo

def get_valor_minimo2(lista):
    minimo = None
    for v in lista:
        if minimo == None:
            minimo = v
        elif v < minimo:
            minimo = v
    return minimo

def main():
    numeros = [10, 25, 36, 45, 3]
    print(get_valor_minimo2(numeros))
    print(get_valor_maximo2(numeros))

if __name__ == '__main__':
    main()