""" Stage Logo View for Recital """
# __doc__ (Stage Logo View Model file for little Recital app for testing
# Queues and Piles)

from pathlib import Path


class StageLogo:
    """
    Class for Stage View Model

    Arguments:
    -

    Returns a orderer ramdom list from 3 optional modes.

    >>> stage_logo = StageLogo()
    string

    TODO:
        -

    """

    @classmethod
    def get_logo(cls, lang: object) -> object:
        """
        Function to get a stage logo in ascii art

        Arguments:
        self

        Returns a stage logo in ascii art from a text file
        inside /app/static/txt (str)

        >>> stage_logo = StageLogo()
        >>> stage_logo.get_logo()
        string

        TODO:
            -
        """

        try:
            content = []
            current_path = Path.cwd()
            txt_path = current_path/'app'/'static'/'txt'/'stage_logo.txt'

            with open(txt_path, 'r', encoding="utf-8") as file:
                content = file.read()
                file.close()

                return content
        except FileNotFoundError as error:
            print(
                lang["LANG"]["LANG_ERROR_READING_TXT"].format(txt_path),
                f'Error: {error}')
            return None
        except KeyError as error:
            print(
                lang["LANG"]["LANG_ERROR_READING_TXT"].format(txt_path),
                f'Error: {error}')
            return None

    def dummy_func(self):
        """ Dummy DocString"""
        return None
