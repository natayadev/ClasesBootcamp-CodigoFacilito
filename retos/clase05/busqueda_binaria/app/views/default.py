""" Default View for BinarySearchAlgorithms"""
# __doc__ (Default View file for little data structure app
# testing Binary Search Algorithms)

import os
import functools


class DefaultView:
    """
    Class for Default View

    Arguments:
    None

    Gets the view for this App.

    >>> view = DefaultView()
    True

    TODO:
        -

    """

    def _decorate_intro(num_lines: int) -> str:  # noqa: E501  # pylint: disable=no-self-argument
        """
        Decorator for intro and exit from app

        Arguments:
        num_lines (int)

        Repeat lines before and after of each intro or exit message (str)

        TODO:
            -
        """

        def decorator_decorate_intro(func: str):

            @functools.wraps(func)
            def wrapped_decorate_intro(self, *args, **kwargs) -> list:
                line = '-'*49+' \n'
                message = ''
                counter_start = counter_end = 1
                while counter_start <= num_lines:
                    message += line
                    counter_start += 1

                message += func(self, *args, **kwargs)

                while counter_end <= num_lines:
                    message += line
                    counter_end += 1

                return message
            return wrapped_decorate_intro
        return decorator_decorate_intro

    @_decorate_intro(num_lines=3)  # pylint: disable=redundant-keyword-arg
    def get_intro(self) -> str:
        """
        Function to get intro view message

        Arguments:
        self

        Prints App intro message (str)

        TODO:
            -
        """
        return '          Binary Search Algorithms  \n'

    @_decorate_intro(num_lines=1)  # pylint: disable=redundant-keyword-arg
    def get_exit(self, lang: object) -> str:
        """
        Function to get exit view message

        Arguments:
        lang (object)

        Prints App exit message (str)

        TODO:
            -
        """
        self.clean_screen()
        return f' >>> {lang["LANG"]["LANG_EXIT_PROGRAM"]} \n'

    def get_menu_options(self, key: str, value: str) -> str:
        """
        Function to get menu options view format

        Arguments:
        key (str)
        value (str)

        Format the Menu Options (str)

        TODO:
            -
        """
        return f'[{key}] {value} '

    def get_input(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the select option input (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_INPUT_SELECT_OPTION"]} ')

    def get_linebrake(self) -> str:
        """
        Function to get a linebrake in view

        Arguments:
        self

        Format the Menu Options (str)

        TODO:
            -
        """
        return '\n'

    def input_language(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the select option input (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_SELECT_LANGUAGE"]} ')

    def input_start(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the select option input (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_INPUT_PRESS_A_KEY_START"]} ')

    def input_pause(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the intro press a key pause (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_INPUT_PRESS_A_KEY_CONTINUE"]} ')

    def input_pause_repeat(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the pause option to repeat binary search (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_INPUT_PRESS_REPEAT_OR_QUIT"]} ')

    def clean_screen(self) -> object:
        """
        Function to make a screen clear in view

        Arguments:
        self

        Make a screen clear in view, cls for Windows, clear for
        Unix/Linux (object)

        TODO:
            -
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def get_data_output(self, lang: object, mode: str, data: list) -> str:
        """
        Function to format the binary search list and data title

        Arguments:
        self
        lang (object)
        mode (str)
        data (list)

        Returns the list[mode] title and the data (str)

        TODO:
            -
        """
        return lang["LANG"]["LANG_OUTPUT_LIST"].format(mode, data)

    def get_input_search(self, lang: object) -> str:
        """
        Function to get an input

        Arguments:
        self
        lang (object)

        Returns the binary search input (str)

        TODO:
            -
        """
        return input(f'{lang["LANG"]["LANG_INPUT_SEARCH_NUMBER"]} ')

    def get_result_output(self, lang: object, result: str) -> str:
        """
        Function to format the binary search result title

        Arguments:
        self
        lang (object)
        result (str)

        Returns the result title and result from binary search (str)

        TODO:
            -
        """
        return lang["LANG"]["LANG_OUTPUT_RESULT"].format(result)
