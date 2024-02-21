def merge_sort(lista: list) -> list:
    if len(lista) <= 1:
        return lista
    else:
        meio = len(lista) // 2
        esquerda = merge_sort(lista[:meio])
        direita = merge_sort(lista[meio:])
        return merge(esquerda, direita)

def merge(esquerda, direita):
    nova_lista = []
    topo_esq, topo_dir = 0, 0
    while topo_esq < len(esquerda) and topo_dir < len(direita):
        if direita[topo_dir] < esquerda[topo_esq]:
            nova_lista.append(direita[topo_dir])
            topo_dir += 1
        else:
            nova_lista.append(esquerda[topo_esq])
            topo_esq += 1
    nova_lista += direita[topo_dir:]
    nova_lista += esquerda[topo_esq:]
    return nova_lista

def main():
    lista = [1, 3, 5, 2, 10, 8, 15, 23, 4, 7]

    print(lista)
    lista = merge_sort(lista)
    print(lista)

if __name__ == "__main__":
    main()