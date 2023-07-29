""" Info file for Multi_Maths Package """
# __doc__ (Info file for testing modules and packages)


class Info():
    """ Info class """

    @classmethod
    def show_credits(cls, print_credits: True) -> object:
        """
            Returns credits
        """
        info = {
            'title': 'Multi Maths Package',
            'version': '1.0.7',
            'date': '2023-06-22',
            'developer': 'Gonzalo Mahserdjian',
            'developer_alias': 'gsmx64',
            'package': 'Bootcamp Código Facilito Python Avanzado',
            'subpackage': 'Class 03 Practice Challenge',
            'class': 'Advanced Algorithms',
            'bootcamp roadmap': 'https://codigofacilito.com/bootcamps/python-avanzado/roadmap',  # noqa: E501  # pylint: disable=line-too-long
            'license': 'GNU/GPL version 3',
            'license link': 'https://www.gnu.org/licenses/gpl-3.0.txt'
        }

        if print_credits:
            for keys, values in info.items():
                print(f'{keys}: {values}')
        return info

    def dummy_func(self):
        """ Dummy DocString"""
        return None
