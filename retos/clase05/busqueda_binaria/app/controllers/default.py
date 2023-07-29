""" Default Controller for BinarySearchAlgorithms"""
# __doc__ (Default Controller file for little data structure app
# testing Binary Search Algorithms)

import configparser

from app.views.default import DefaultView
from app.models.algorithms.binary import AlgorithmBinarySearch
from app.models.random_data import RamdomData


class DefaultController:
    """
    Class for Default Controller

    Arguments:
    None

    Runs the App.

    >>> run = DefaultController
    >>> run.run_app()
    True

    TODO:
        -

    """

    @classmethod
    def show_credits(cls, print_credits: True) -> object:
        """
        Class-Method to return credits

        Arguments:
        cls
        print_credits (boolean)

        Prints at exit the app all credits if print_credits is True,
        else returns a dictionary with credits (str/dict)

        TODO:
            -
        """
        info = {
            'title': 'Binary Search Algorithms',
            'version': '1.0.0',
            'date': '2023-06-10',
            'developer': 'Gonzalo Mahserdjian',
            'developer_alias': 'gsmx64',
            'package': 'Bootcamp Código Facilito Python Avanzado',
            'subpackage': 'Class 05 Practice Challenge',
            'class': 'Advanced Data Structures',
            'bootcamp roadmap': 'https://codigofacilito.com/bootcamps/python-avanzado/roadmap',  # noqa: E501  # pylint: disable=line-too-long
            'license': 'GNU/GPL version 3',
            'license link': 'https://www.gnu.org/licenses/gpl-3.0.txt'
        }

        if print_credits:
            for keys, values in info.items():
                print(f'{keys}: {values}')

        return info

    @classmethod
    def create_app(cls) -> object:
        """
        Class-Method to inits the app

        Arguments:
        cls

        Inits this App (object)

        TODO:
            -
        """
        cls.cfg = configparser.ConfigParser()
        cls.cfg.sections()
        cls.cfg.read('app/config.ini', 'UTF-8')

        cls.lang = configparser.ConfigParser()
        cls.lang.sections()
        cls.lang.read('app/languages/'+cls.cfg["LANGUAGE"]
                      ["DEFAULT_LANGUAGE"]+'.ini', 'UTF-8')

        cls.view = DefaultView()
        cls.binary_search = AlgorithmBinarySearch()

        random_data = RamdomData()
        random_data.mode = cls.cfg["RANDOMDATA"]["RANDOMDATA_MODE"]
        random_data.amounth = cls.cfg.getint(
            "RANDOMDATA", "RANDOMDATA_AMOUNTH")
        random_data.max = cls.cfg.getint("RANDOMDATA", "RANDOMDATA_MAX")
        cls.data = random_data.get_data

        cls.view.clean_screen()
        print(cls.view.get_intro())

        current_language_input = cls.view.input_language(cls.lang)
        current_language = cls.current_language(
            cls, current_language_input,
            cls.cfg["LANGUAGE"]["DEFAULT_LANGUAGE"])
        cls.lang.read('app/languages/'+current_language+'.ini', 'UTF-8')

        cls.view.input_start(cls.lang)
        cls.view.clean_screen()

        cls._go_to_menu(cls)
        print(cls.view.get_exit(cls.lang))

    def _go_to_menu(self) -> object:
        """
        Function to build the first level menu options

        Arguments:
        self

        Builds the first level menu options (object)

        TODO:
            -
        """
        print(self.view.get_intro())

        menus = {'1': self.lang["LANG"]["LANG_RUN_BINARY_SEARCH"],
                 'Q': self.lang["LANG"]["LANG_QUIT_LEYEND"]}

        for index, value in menus.items():
            print(self.view.get_menu_options(index, value))

        print(self.view.get_linebrake(), end='')
        option = self.view.get_input(self.lang)

        if option in menus.keys() and option.lower() != 'q':  # noqa: E501  # pylint: disable=consider-iterating-dictionary
            self._go_to_option(self)  # noqa: E501  # pylint: disable=too-many-function-args

        elif option.lower() == 'q':
            print(self.view.get_exit(self.lang))
        else:
            self.view.clean_screen()
            self._go_to_menu(self)  # noqa: E501  # pylint: disable=too-many-function-args
            self.view.clean_screen()

    def _go_to_option(self) -> object:
        """
        Function to build the first level menu options

        Arguments:
        self

        Builds the first level menu options (object)

        TODO:
            -
        """
        check = ''
        while check != 'q':
            self.view.clean_screen()
            print(self.view.get_intro())
            print(self.view.get_data_output(
                self.lang,
                self.cfg["RANDOMDATA"]["RANDOMDATA_MODE"],
                self.data))
            print(self.view.get_linebrake(), end='')

            search_value = self.view.get_input_search(self.lang)
            if not search_value.isnumeric():
                continue

            print(self.view.get_result_output(
                self.lang,
                self.binary_search.get(self.lang, self.data, search_value)))
            print(self.view.get_linebrake(), end='')

            check = self.view.input_pause_repeat(self.lang)
        else:  # noqa: E501  # pylint: disable=useless-else-on-loop
            self.view.clean_screen()
            self._go_to_menu(self)  # noqa: E501  # pylint: disable=too-many-function-args
            self.view.clean_screen()

    def current_language(self, current_language_input: str,
                         default_language='en') -> str:
        """
        Function to get current short language code

        Arguments:
        self
        current_language_input (str)
        default_language (str)

        Get from first input the current short language code or default
        language from config (str)

        TODO:
            -
        """
        if current_language_input == '1':
            current_language = 'en'
        elif current_language_input == '2':
            current_language = 'es'
        else:
            current_language = default_language
        return current_language
