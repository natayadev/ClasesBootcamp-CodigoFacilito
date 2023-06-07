def busqueda_binaria(lista, valor_buscado):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        mitad = (final+inicio)//2
        print(mitad)

        if lista[mitad] == valor_buscado:
            return True
        elif lista[mitad] > valor_buscado:
            final = mitad - 1
            print("El valor buscado es menor")
        elif lista[mitad] < valor_buscado:
            inicio = mitad + 1
            print("El valor buscado es mayor")
    return False

if __name__ == "__main__":
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    valor_buscado = 6

    print(busqueda_binaria(lista, valor_buscado))