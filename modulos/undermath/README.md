# Undermath

Este paquete contiene módulos para realizar cálculos aritméticos y estadísticos sencillos.

[Documentación completa en readthedocs.io](https://undermath.readthedocs.io/en/latest/)

## Uso como script

    python3 main.py <operación> <operandos separados por espacios>

### Operaciones aritméticas soportadas:

    -sum, --sumar <operandos separados por espacios>
        Suma dos o más operandos de tipo int o float separados por espacios.

    -dif, --restar <operandos separados por espacios>
        Resta al primer operando el segundo.

    -mult, --multiplicar <operandos separados por espacios>
        Multiplica dos o más operandos de tipo int o float.

    -div, --dividir <operandos separados por espacios>
        Divide el primer operando entre el segundo.

### Funciones estadísticas soportadas:

    -med, --media <operandos separados por espacios>
        Obtiene la media de una lista de elementos enteros o flotantes separados por espacios.

    -mdn, --mediana <operandos separados por espacios>
        Obtiene la mediana de una lista de elementos enteros o flotantes separados por espacios.

    -mod, --moda <operandos separados por espacios>
        Obtiene la moda de una lista de elementos enteros o flotantes separados por espacios.

    -dsm,--desviacion-estandar-muestral <operandos separados por espacios>
        Obtiene la desviación estándar muestral de una lista de elementos enteros o flotantes separados por espacios.

    -dsp, --desviacion-estandar-poblacional <operandos separados por espacios>
        Obtiene la desviación estándar poblacional de una lista de elementos enteros o flotantes separados por espacios.

## Uso como módulo

### Operaciones aritméticas

    >>> from undermath.modulos_aritmeticos.operaciones_basicas import *
    >>> sumar([1, 2, 3])
    Resultado de la suma: 6.0
    >>> restar([4, 2])
    Resultado de la resta: 2.0
    >>> multiplicar([3, 5, 7])
    Resultado de la multiplicacion: 105.0
    >>> dividir([15, 3])
    Resultado de la división: 5.0

### Funciones estadísticas

    >>> from undermath.modulos_estadisticos.funciones_estadisticas import *
    >>> media([1, 2, 3, 4, 5])
    La media es: 3.0
    >>> mediana([1, 2, 3, 4, 5, 6, 7, 8])
    La mediana es: 4.5
    >>> moda([5, 3, 1, 4, 4, 2])
    La moda es: 4
    >>> desviacion_estandar_muestral([5, 3, 1, 4, 4, 2])
    La desviación estándar muestral es: 1.4719601443879744
    >>> desviacion_estandar_poblacional([5, 3, 1, 4, 4, 2])
    La desviación estándar poblacional es: 1.3437096247164249
