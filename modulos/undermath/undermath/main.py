""" Módulo para realizar operaciones aritméticas y funciones estadísticas. """

import argparse
from modulos_aritmeticos.operaciones_basicas import *
from modulos_estadisticos.funciones_estadisticas import *


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Módulo para realizar \
                                     operaciones aritméticas y funciones \
                                     estadísticas.')
    parser.add_argument('-sum', '--sumar', dest='sumar', metavar='número',
                        nargs='+', help='sumar dos o más operandos.')
    parser.add_argument('-dif', '--restar', dest='restar', metavar='número',
                        nargs=2,
                        help='restar el segundo operando del primero.')
    parser.add_argument('-mult', '--multiplicar', dest='multiplicar',
                        metavar='número',
                        nargs='+', help='multiplicar dos o más números.')
    parser.add_argument('-div', '--dividir', dest='dividir', metavar='número',
                        nargs=2,
                        help='dividir el primer operando entre el segundo.')
    parser.add_argument('-med', '--media', dest='media', metavar='número',
                        nargs='+',
                        help='obtiene la media de dos o más operandos.')
    parser.add_argument('-mdn', '--mediana', dest='mediana', metavar='número',
                        nargs='+',
                        help='obtiene la mediana de dos o más operandos.')
    parser.add_argument('-mod', '--moda', dest='moda', metavar='número',
                        nargs='+',
                        help='obtiene la moda de dos o más operandos.')
    parser.add_argument('-dsm', '--desviacion-estandar-muestral', dest='dsm',
                        metavar='número', nargs='+',
                        help='obtiene la desviación estándar muestral de dos o\
 más operandos.')
    parser.add_argument('-dsp', '--desviacion-estandar-poblacional',
                        dest='dsp', metavar='número', nargs='+',
                        help='obtiene la desviación estándar poblacional \
de dos o más operandos.')

    args = parser.parse_args()

    if args.sumar:
        sumar(args.sumar)
    if args.restar:
        restar(args.restar)
    if args.multiplicar:
        multiplicar(args.multiplicar)
    if args.dividir:
        dividir(args.dividir)
    if args.media:
        media(args.media)
    if args.mediana:
        mediana(args.mediana)
    if args.moda:
        moda(args.moda)
    if args.dsm:
        desviacion_estandar_muestral(args.dsm)
    if args.dsp:
        desviacion_estandar_poblacional(args.dsp)
