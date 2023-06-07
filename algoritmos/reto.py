from random import sample

"""
CONSIGNA:
Crear una función que realice una búsqueda binaria en una lista generada con el módulo random,
de hasta 100 elementos y que me permita introducir el elemento a buscar por el usuario (input)
"""

def busqueda_binaria(lista, valor):
    # Inicializar el extremo inferior o inicial al primer elemento de la lista
    inicio = 0
    # Inicializar el extremo superior o final al último elemento de la lista
    final = len(lista) - 1


    while inicio <= final:
        mitad = (final + inicio) // 2 # Calcular el valor medio de la lista

        if lista[mitad] == valor:
            # Si el valor del medio es igual que el valor buscado, devuelve True
            return True
        elif lista[mitad] > valor:
            # Si el valor del medio es mayor que el valor buscado, ajustar el extremo superior de la lista
            final = mitad - 1
        elif lista[mitad] < valor:
            # Si el valor del medio es menor que el valor buscado, ajustar el extremo inferior de la lista
            inicio = mitad + 1

    # Si el valor del medio no es encontrado en la lista, devuelve False
    return False

if __name__ == "__main__":
    lista_aleatoria = sample(range(0, 999), 100) #Generar la lista con 100 números enteros aleatorios
    lista_aleatoria.sort()  # Ordenar la lista de mayor a menor
    print(lista_aleatoria)
    valor_buscado = int(input("Hola, introducir un número: "))

    print(busqueda_binaria(lista_aleatoria, valor_buscado))