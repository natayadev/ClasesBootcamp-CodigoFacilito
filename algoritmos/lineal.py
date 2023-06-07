def busqueda_lineal(lista,valor_buscado):
    for i in range(len(lista)):
        if lista[i] == valor_buscado:
            return True
    return False

if __name__ == "__main__":
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    valor_buscado = 26

    print(busqueda_lineal(lista,valor_buscado))