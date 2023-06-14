class FilaAsistentes:
    """ Clase para definir una fila generica para usarse
        en la cola de entrada de asistentes y en los lugares del
        recital
    """
    def __init__(self):
        """ Inicializa una lista vacía de asistentes
        """
        self._lugares = []

    def ingresar_asistente(self, asistente):
        """ Agrega un asistente al final de la cola o recital

        Args:
            asistente (str): string con el nombre del asistente
        """
        self._lugares.append(asistente)

    def salida_asistente(self):
        """ Retira un asistente del inicio de la cola o recital

        Returns:
            str: nombre del asistente que salió
        """
        return self._lugares.pop(0)


if __name__ == '__main__':
    fila_ingreso = FilaAsistentes()
    recital = FilaAsistentes()

    print(f'Hay {len(fila_ingreso._lugares)} asistente(s) en fila de ingreso:\
          {fila_ingreso._lugares}')
    for asistente in range(10):
        input('Presiona Enter para formar un asistente en la fila.\n')
        fila_ingreso.ingresar_asistente(f'asistente_{asistente + 1}')
        print(f'Hay {len(fila_ingreso._lugares)} asistente(s) en fila de\
ingreso: {fila_ingreso._lugares}\n')
    print('\n¡Se completó la fila para entrar al recital!\n')
    print(f'Hay {len(recital._lugares)} asistentes dentro del recital:\
        {recital._lugares}')
    for asistente in fila_ingreso._lugares.copy():
        input('Presiona Enter para ingresar un asistente al recital.\n')
        recital.ingresar_asistente(fila_ingreso.salida_asistente())
        print(f'Hay {len(fila_ingreso._lugares)} asistente(s) en fila de\
ingreso: {fila_ingreso._lugares}')
        print(f'Hay {len(recital._lugares)} asistente(s) dentro del recital:\
{recital._lugares}\n')
    print('\n¡Han ingresado todos los asistentes al recital recital!\n')
    for asistente in recital._lugares.copy():
        input('Presiona Enter para sacar un asistente del recital.\n')
        asistente_fuera = recital.salida_asistente()
        print(f'Salió el asistente: {asistente_fuera}')
        print(f'Hay {len(recital._lugares)} asistente(s) dentro del recital:\
{recital._lugares}\n')
    print('\n¡Han salido todos los asistentes del recital!\n')
