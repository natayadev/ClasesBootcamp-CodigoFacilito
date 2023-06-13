import random


def busqueda_binaria(lista, elemento):
    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        valor_medio = lista[medio]

        if valor_medio == elemento:
            return medio
        elif valor_medio < elemento:
            inicio = medio + 1
        else:
            final = medio - 1

    return -1


lista = random.sample(
    range(1, 101), random.randint(1, 100)
)

lista.sort()
elemento = int(input("Ingrese el elemento a buscar: "))
indice = busqueda_binaria(lista, elemento)

if indice != -1:
    print(f"El elemento {elemento} se encuentra en el índice {indice} de la lista.")
else:
    print("El elemento no pertenece a esta lista.")
