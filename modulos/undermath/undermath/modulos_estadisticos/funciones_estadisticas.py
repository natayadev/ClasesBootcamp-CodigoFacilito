from typing import List


def validar_entrada(valores: List = []):
    """
    Esta función acepta una lista y determina si todos los valores se \
pueden convertir a flotante.

    Args:
        valores (List): Una lista con valores de tipo string.

    Regresa:
        List: Una lista con los valores convertidos a flotantes.
        False (Bool): si no todos los valores de la lista se pudieron \
convertir.

    Ejemplos de uso:

    >>> validar_entrada(["1", "2", "3"])
    [1.0, 2.0, 3.0]

    Ejemplo de error:

    >>> validar_entrada([1, "t"])
    False
    """

    lista_flotantes = []
    for valor in valores:
        try:
            lista_flotantes.append(float(valor))
        except ValueError:
            return False
    return lista_flotantes


def media(valores: List = []):
    """
    Esta función acepta una lista con enteros o flotantes y obtiene \
la media o promedio.

    Args:
        valores (List): Una lista con valores de tipo string.

    Regresa:
        str: "La media es: <resultado>".

    Ejemplos de uso:

    >>> media(["1", "2", "3"])
    La media es: 2.0

    Ejemplo de error:

    >>> media([1, "t", 3, 4])
    Únicamente puedes usar números enteros o flotantes.
    """

    media = 0
    for valor in valores:
        try:
            valor = float(valor)
        except ValueError:
            print("Únicamente puedes usar números enteros o flotantes.")
            return
        media += valor
    if isinstance(media, float):
        print(f"La media es: {media/len(valores)}")


def mediana(valores: List = []):
    """
    Esta función acepta una lista con enteros o flotantes y obtiene \
la mediana.

    Args:
        valores (List): Una lista con valores de tipo string.

    Regresa:
        str: "La mediana es: <resultado>".

    Ejemplos de uso:

    >>> mediana(["1", "2", "3"])
    La mediana es: 2.0

    Ejemplo de error:

    >>> mediana([1, "t", 3, 4])
    Únicamente puedes usar números enteros o flotantes.
    """

    if validar_entrada(valores):
        mediana = 0
        valores.sort()
        mitad = len(valores) // 2
        mediana = (float(valores[mitad]) + float(valores[~mitad])) / 2
        print(f"La mediana es: {mediana}")
    else:
        print("Únicamente puedes usar números enteros o flotantes.")


def moda(valores: List = []):
    """
    Esta función acepta una lista con enteros o flotantes y obtiene \
la moda.

    Args:
        valores (List): Una lista con valores de tipo string.

    Regresa:
        str: "La moda es: <resultado>".

    Ejemplos de uso:

    >>> moda(["5", "3", "1", "4", "4", "2"])
    La moda es: 4

    Ejemplo de error:

    >>> moda([1, "t", 3, 4])
    Únicamente puedes usar números enteros o flotantes.
    """

    if validar_entrada(valores):
        print(f"La moda es: {max(set(valores), key=valores.count)}")
    else:
        print("Únicamente puedes usar números enteros o flotantes.")


def desviacion_estandar_muestral(valores: List = []):
    """
    Esta función acepta una lista con enteros o flotantes y obtiene \
la desviación estándar muestral.

    Args:
        valores (List): Una lista con valores de tipo string.

    Regresa:
        str: "La desviación estándar muestral es: <resultado>".

    Ejemplos de uso:

    >>> desviacion_estandar_muestral(["5", "3", "1", "4", "4", "2"])
    La desviación estándar muestral es: 1.4719601443879744

    Ejemplo de error:

    >>> desviacion_estandar_muestral([1, "t", 3, 4])
    Únicamente puedes usar números enteros o flotantes.
    """

    if validar_entrada(valores):
        valores = validar_entrada(valores)
        print(f"La desviación estándar muestral es: \
{(sum((float(x)-(sum(valores) / len(valores)))**2 for x in valores) / (len(valores)-1))**0.5}")
    else:
        print("Únicamente puedes usar números enteros o flotantes.")


def desviacion_estandar_poblacional(valores: List = []):
    """
    Esta función acepta una lista con enteros o flotantes y obtiene \
la desviación estándar poblacional.

    Args:
        valores (List): Una lista con valores de tipo string.

    Regresa:
        str: "La desviación estándar poblacional es: <resultado>".

    Ejemplos de uso:

    >>> desviacion_estandar_poblacional(["5", "3", "1", "4", "4", "2"])
    La desviación estándar poblacional es: 1.3437096247164249

    Ejemplo de error:

    >>> desviacion_estandar_poblacional([1, "t", 3, 4])
    Únicamente puedes usar números enteros o flotantes.
    """

    if validar_entrada(valores):
        valores = validar_entrada(valores)
        print(f"La desviación estándar poblacional es: \
{(sum((float(x)-(sum(valores) / len(valores)))**2 for x in valores) / (len(valores)))**0.5}")
    else:
        print("Únicamente puedes usar números enteros o flotantes.")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
