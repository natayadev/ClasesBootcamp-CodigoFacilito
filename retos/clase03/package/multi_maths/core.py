""" Core file for Multi_Maths Package """
# __doc__ (Core file for testing modules and packages)

import os
import configparser
from importlib.resources import files

from multi_maths.mm_arithmetic import mm_arithmetic as mm_am
from multi_maths.mm_geometry import mm_geometry as mm_ge
from multi_maths.mm_statistics import mm_statistics as mm_st


class Core:
    """ Core class """

    _lang = ''
    _lang_name = ''
    _response = ''
    _module = ''
    _submodule = ''
    _args = tuple()

    def __init__(self) -> object:
        """Init"""
        return None

    @property
    def lang(self):
        """
        Set default language object, (en) for default
        """

        lang_file = files("multi_maths").joinpath(f'languages/{self._lang_name}.ini')  # noqa: E501  # pylint: disable=C0301

        if os.path.exists(lang_file) is False:
            lang_file = files("multi_maths").joinpath('languages/en.ini')  # noqa: E501  # pylint: disable=C0301

        lang = configparser.ConfigParser()
        lang.sections()
        lang.read(lang_file, 'UTF-8')

        return lang

    def set_lang(self, _lang_name='en') -> object:
        """
        Set default language name tag, (en) for default
        """
        self._lang_name = _lang_name.lower()
        return self._lang_name

    def set_response(self, response_str: str) -> str:
        """
        Check response format tag
        """
        try:
            self._response = response_str.lower()
            assert_msg = self.lang["LANG"]["LANG_ERROR_RESPONSE_OPTION"].format(response_str)  # noqa: E501  # pylint: disable=C0301
            assert self._response in ('text', 'digit'), assert_msg  # noqa: E501  # pylint: disable=C0301
            return self._response
        except AssertionError as error:
            return print(error)

    @property
    def get_response(self):
        """
        Get response format
        """
        return self._response

    def run(self, module: str, submodule: str, args: tuple):  # noqa: E501  # pylint: disable=R0911,R0912,C0301
        """
        Retrieve modules and submodules
        """

        self._module = module
        self._submodule = submodule
        self._args = args

        if self._module == 'ari':
            module_aritmetic = mm_am.MM_Arithmetic(self.lang, self._response)
            if self._submodule == 'add':  # pylint: disable=R1705
                return module_aritmetic.addition(self._args)
            elif self._submodule == 'sub':
                return module_aritmetic.subtraction(self._args)
            elif self._submodule == 'mul':
                return module_aritmetic.multiplication(self._args)
            elif self._submodule == 'div':
                return module_aritmetic.division(self._args)
            elif self._submodule == 'mod':
                return module_aritmetic.modulus(self._args)
            elif self._submodule == 'exp':
                return module_aritmetic.exponentiation(self._args)
            elif self._submodule == 'flo':
                return module_aritmetic.floor_division(self._args)
            else:
                return self.lang["LANG"]["LANG_ERROR_SUBM_ARI"]
        elif self._module == 'geo':
            module_geometry = mm_ge.MM_Geometry(self.lang, self._response)
            if self._submodule == 'ca':  # pylint: disable=R1705
                return module_geometry.circle_area(self._args[0])
            elif self._submodule == 'cc':
                return module_geometry.circle_circumference(self._args[0])
            elif self._submodule == 'ta':
                return module_geometry.triangle_area(self._args)
            elif self._submodule == 'tp':
                return module_geometry.triangle_perimeter(self._args)
            elif self._submodule == 'sa':
                return module_geometry.square_area(self._args)
            elif self._submodule == 'sp':
                return module_geometry.square_perimeter(self._args)
            elif self._submodule == 'ra':
                return module_geometry.rectangle_area(self._args)
            elif self._submodule == 'rp':
                return module_geometry.rectangle_perimeter(self._args)
            elif self._submodule == 'pa':
                return module_geometry.parallelogram_area(self._args)
            elif self._submodule == 'pp':
                return module_geometry.parallelogram_perimeter(self._args)
            else:
                return self.lang["LANG"]["LANG_ERROR_SUBM_GEO"]
        elif self._module == 'stat':
            module_statistics = mm_st.MM_Statistics(self.lang, self._response)
            if self._submodule == 'sd':  # pylint: disable=R1705
                if len(self._args) >= 1:
                    return module_statistics.standard_deviation(
                        self._args[0], 0)
                return module_statistics.standard_deviation(
                    self._args[0], self._args[1])
            elif self._submodule == 'mean':
                return module_statistics.mean(self._args[0])
            elif self._submodule == 'med':
                return module_statistics.median(self._args[0])
            elif self._submodule == 'mode':
                return module_statistics.mode(self._args[0])
            else:
                return self.lang["LANG"]["LANG_ERROR_SUBM_STAT"]

        return self.lang["LANG"]["LANG_ERROR_MODULE_ROOT"]


def _run() -> object:
    """
        Instancer for Core() class
    """

    return Core()
