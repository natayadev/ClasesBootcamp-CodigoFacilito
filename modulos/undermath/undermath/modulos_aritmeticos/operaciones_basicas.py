from typing import List


def sumar(valores: List = []):
    """
    Esta función acepta una lista con enteros o flotantes y los suma.

    Args:
        valores (List): Una lista con valores enteros o flotantes.

    Regresa:
        float: La suma de los valores en la lista.

    Ejemplos de uso:

    >>> sumar([1, 2, 3])
    Resultado de la suma: 6.0

    Ejemplo de error:

    >>> sumar([1, "t"])
    Únicamente puedes sumar números enteros o flotantes.
    """

    suma = 0
    for valor in valores:
        try:
            valor = float(valor)
        except ValueError:
            print("Únicamente puedes sumar números enteros o flotantes.")
            return
        suma += valor
    if isinstance(suma, float):
        print(f"Resultado de la suma: {suma}")


def restar(valores: List = []):
    """
    Esta función acepta una lista con dos enteros o flotantes y los resta.

    Args:
        valores (List): Una lista con dos valores enteros o flotantes.

    Regresa:
        float: La resta del primer valor menos el segundo.

    Ejemplos de uso:

    >>> restar([2, 1])
    Resultado de la resta: 1.0

    Ejemplo de error:

    >>> restar([1, "t"])
    Únicamente puedes restar números enteros o flotantes.
    """

    resta = 0
    try:
        valores[0] = float(valores[0])
        valores[1] = float(valores[1])
        resta = valores[0] - valores[1]
    except ValueError:
        print("Únicamente puedes restar números enteros o flotantes.")
        return
    if isinstance(resta, float):
        print(f"Resultado de la resta: {resta}")


def multiplicar(valores: List = []):
    """
    Esta función multiplica los valores enteros o flotantes de una lista.

    Args:
        valores (List): Una lista con valores enteros o flotantes.

    Regresa:
        float: La multiplicación de los valores en la lista.

    Ejemplos de uso:

    >>> multiplicar([3, 6])
    Resultado de la multiplicacion: 18.0

    >>> multiplicar([0, 10])
    Resultado de la multiplicacion: 0.0

    Ejemplo de error:

    >>> multiplicar([1, "t"])
    Únicamente puedes multiplicar números enteros o flotantes.
    """

    multiplicacion = 1
    for valor in valores:
        try:
            valor = float(valor)
        except ValueError:
            multiplicacion = None
            print("Únicamente puedes multiplicar números enteros o flotantes.")
            return
        multiplicacion *= valor
    if isinstance(multiplicacion, float):
        print(f"Resultado de la multiplicacion: {multiplicacion}")


def dividir(valores: List = []):
    """
    Esta función divide el valor[0] entre el valor[1] de una lista de enteros \
o flotantes.

    Args:
        valores (List): Una lista con valores enteros o flotantes.

    Regresa:
        float: La división del primer valor entre el segundo.

    Ejemplos de uso:

    >>> dividir([6, 2])
    Resultado de la división: 3.0

    >>> dividir([0, 10])
    Resultado de la división: 0.0

    Ejemplos de error:

    >>> dividir([10, 0])
    No puedes dividir entre cero.

    >>> dividir([10, "t"])
    Únicamente puedes dividir números enteros o flotantes.
    """

    division = 0
    try:
        valores[0] = float(valores[0])
        valores[1] = float(valores[1])
        division = valores[0] / valores[1]
    except ValueError:
        print("Únicamente puedes dividir números enteros o flotantes.")
    except ArithmeticError:
        print("No puedes dividir entre cero.")
        return
    if isinstance(division, float):
        print(f"Resultado de la división: {division}")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
