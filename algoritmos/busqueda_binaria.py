import random


def busqueda_binaria(lista, valor_buscado):
    """ Realiza una búsqueda binaria en una lista ordenada

    Args:
        lista (List): lista ordenada con valores enteros
        valor_buscado (int): valor a buscar

    Returns:
        bool: True o False dependiendo si el valor buscado está en la lista
    """
    if lista == []:
        return False
    elif len(lista) == 1:
        return lista[0] == valor_buscado
    else:
        indice_elemento_medio = len(lista) // 2
        if valor_buscado == lista[indice_elemento_medio]:
            return True
        elif valor_buscado < lista[indice_elemento_medio]:
            print(f"Valor buscado {valor_buscado} es menor que \
el valor a la mitad de la lista: {lista[indice_elemento_medio]}")
            print(f"Nueva lista será {lista[:indice_elemento_medio:]}")
            return busqueda_binaria(lista[:indice_elemento_medio:],
                                    valor_buscado)
        else:
            print(f"Valor buscado {valor_buscado} es mayor que \
el valor a la mitad de la lista: {lista[indice_elemento_medio]}")
            print(f"Nueva lista será {lista[indice_elemento_medio + 1::]}")
            return busqueda_binaria(lista[indice_elemento_medio + 1::],
                                    valor_buscado)


if __name__ == "__main__":
    lista_aleatorios = []
    for x in range(random.randint(1, 100)):
        for elemento_aleatorio in random.sample(
                range(random.randint(1, 100)), 1):
            if elemento_aleatorio not in lista_aleatorios:
                lista_aleatorios.append(elemento_aleatorio)
    print(f"Lista con {len(lista_aleatorios)} elementos aleatorios:\
{lista_aleatorios}")
    lista_aleatorios.sort()
    print(f"Lista ordenada: {lista_aleatorios}")
    elemento_a_buscar = int(input("Introduce el elemento a buscar: "))
    if busqueda_binaria(lista_aleatorios, elemento_a_buscar):
        print(f"El elemento {elemento_a_buscar} sí está en la lista.")
    else:
        print(f"El elemento {elemento_a_buscar} no está en la lista.")
