from OrdenarNumeros import main as mn

def buscar(elemento, lista):
    minimo = 0
    maximo = len(lista) - 1
    encontrado = False

    while minimo <= maximo and not encontrado:
        meio = (maximo + minimo) // 2
        if elemento == lista[meio]:
            encontrado = True
        elif elemento > lista[meio]:
            minimo = meio + 1
        elif elemento < lista[meio]:
            maximo = meio - 1
    return encontrado

def main():
    lista = ['d','b','a', 'c']
    elemento = input("Que elemento você que buscar? ")
    lista = mn.merge_sort(lista)
    existe = buscar(elemento, lista)

    if existe:
        print(f"O elemento {elemento} existe na lista!")
    else:
        print(f"O elemento {elemento} não existe na lista!")

if __name__ == "__main__":
    main()