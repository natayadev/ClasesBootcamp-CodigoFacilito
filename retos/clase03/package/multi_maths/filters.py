""" Filters file for Multi_Maths Package """
# __doc__ (Filters file for testing modules and packages)


class Filters:
    """ Filters class """

    def __init__(self, lang: object) -> None:
        """
            Init Filters() class requirements
        """

        self.lang = lang

    def value(self, value):
        """
            Returns a float or int value
        """

        try:
            value_str = str(value)

            if value_str.replace('.', '', 1).isdigit():
                return float(value)

            if value_str.isnumeric():
                return int(value)

            raise Exception(f'Error: {value}')  # pylint: disable=W0719
        except Exception as error:
            raise error

    def dummy_func(self):
        """ Dummy DocString"""
        return None


def _run(lang: object) -> object:
    """
        Instancer for Filters() class
    """

    return Filters(lang)
