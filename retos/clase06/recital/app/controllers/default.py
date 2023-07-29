""" Default Controller for Recital """
# __doc__ (Default Controller file little Recital app for testing
# Queues and Piles)

import configparser

# from app.controllers.stage import StageController
from app.views.default import DefaultView
from app.views.stage import StageView
from app.models.queues import QueueData


class DefaultController():
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
            'title': 'Recital',
            'version': '1.0.0',
            'date': '2023-06-12',
            'developer': 'Gonzalo Mahserdjian',
            'developer_alias': 'gsmx64',
            'package': 'Bootcamp Código Facilito Python Avanzado',
            'subpackage': 'Class 06 Practice Challenge',
            'class': 'Advanced Data Structures',
            'bootcamp roadmap': 'https://codigofacilito.com/bootcamps/python-avanzado/roadmap',  # noqa: E501  # pylint: disable=C0301
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

        menus = {'1': self.lang["LANG"]["LANG_RUN_RECITAL_QUEUE"],
                 'Q': self.lang["LANG"]["LANG_QUIT_LEYEND"]}

        for index, value in menus.items():
            print(self.view.get_menu_options(index, value))

        print(self.view.get_linebrake(), end='')
        option = self.view.get_input(self.lang)
        print(option)
        if option.upper() in menus.keys() or option.lower() in menus.keys() and option.lower() != 'q':  # noqa: E501  # pylint: disable=C0201,C0301

            if option == '1':
                self.pit_list = []  # pylint: disable=W0201
                self.queue_list = []  # pylint: disable=W0201
                self.queues = QueueData(  # pylint: disable=W0201
                    self.pit_list, self.queue_list, self.lang, self.cfg)
                self.view_stage = StageView(  # pylint: disable=W0201
                    self.queues, self.lang)  # pylint: disable=W0201

                self._go_to_option(self)  # pylint: disable=E1121
            if option.lower() == 'q':
                print(self.view.get_exit(self.lang))
        else:
            self.view.clean_screen()
            self._go_to_menu(self)  # pylint: disable=E1121

    def _go_to_option(self) -> object:  # pylint: disable=R0912
        """
        Function to build the first level menu options

        Arguments:
        self

        Builds the first level menu options (object)

        TODO:
            -
        """
        check = '*'
        check_options = ['a', 'b', 'c', 'q', '*']
        if check.lower() in check_options:
            self.view.clean_screen()
            print(self.view_stage.get_stage)

            if check.lower() != 'q':
                check = self.view.input_generic(
                    self.lang["LANG"]["LANG_INPUT_SELECT_STAGE_OPTIONS"])

            if check == '1':
                if self.queues.list_full(self.queue_list, self.lang["LANG"]["LANG_INPUT_FREE_QUEUE"]):  # noqa: E501  # pylint: disable=C0301

                    self.view.input_generic(
                        self.lang["LANG"]["LANG_INPUT_STAGE_COMPLETE"])
                else:
                    queue_user = self.view.input_generic(
                        self.lang["LANG"]["LANG_INPUT_STAGE_QUEUE_INSERT"])

                    self.queues.list_add(self.queue_list, self.lang["LANG"]["LANG_INPUT_FREE_QUEUE"],  # noqa: E501  # pylint: disable=C0301
                                         queue_user)

            if check == '2':
                if self.queues.list_empty(self.queue_list, self.lang["LANG"]["LANG_INPUT_FREE_QUEUE"]):  # noqa: E501  # pylint: disable=C0301

                    self.view.input_generic(
                        self.lang["LANG"]["LANG_INPUT_STAGE_QUEUE_EMPTY"])
                else:
                    pit_top = self.queues.list_top(
                        self.queue_list,
                        self.lang["LANG"]["LANG_INPUT_FREE_QUEUE"])

                    pit_check = self.view.input_generic(
                        self.lang["LANG"]["LANG_INPUT_STAGE_QUEUE_TO_PIL"]
                        .format(pit_top))

                    if pit_check.lower() == 'y':
                        self.queues.queue_to_pil(
                            self.queue_list,
                            self.lang["LANG"]["LANG_INPUT_FREE_QUEUE"],
                            self.pit_list,
                            self.lang["LANG"]["LANG_INPUT_FREE_SEAT"])
                        print(
                            self.lang["LANG"]["LANG_INPUT_STAGE_PIL_IN"]
                            .format(pit_top))

            if check == '3':
                while True:
                    try:
                        next(self.queues.pit_remove_generator(self.pit_list))
                    except StopIteration:
                        self.view.input_generic(
                            self.lang["LANG"]["LANG_INPUT_STAGE_PIL_EXIT"])
                        break
                self.view.clean_screen()
                self._go_to_menu(self)  # pylint: disable=E1121

            if check.lower() == 'q':
                self.view.clean_screen()
                self._go_to_menu(self)  # pylint: disable=E1121

            if check.lower() != 'q' and check.lower() != '3':
                self._go_to_option(self)  # pylint: disable=E1121

        else:  # noqa: E501
            self.view.clean_screen()
            self._go_to_option(self)  # noqa: E501  # pylint: disable=E1121
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
