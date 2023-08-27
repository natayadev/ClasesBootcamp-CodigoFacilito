""" Arithmetic Test file for Multi_Maths Package """
# __doc__ (Arithmetic Test file for testing modules and packages)

import configparser
from importlib.resources import files
import unittest

from multi_maths.mm_arithmetic.mm_arithmetic import MM_Arithmetic


class TestArithmetic(unittest.TestCase):
    """
    Class for unittest Arithmetic
    """

    def setUp(self):
        """
        Instance the MM_Arithmetic()
        """

        lang_file = files("multi_maths").joinpath('languages/en.ini')  # noqa: E501  # pylint: disable=C0301
        self.lang = configparser.ConfigParser()
        self.lang.sections()
        self.lang.read(lang_file, 'UTF-8')

        self.aritmetic = MM_Arithmetic(self.lang, 'digit')

    def test_multiplication(self):
        """
        multiplication() test for unittest
        """

        test = self.aritmetic.multiplication((3, 3, 2))
        resolve = 18.0

        self.assertEqual(test, resolve)

    def test_modulus(self):
        """
        modulus() test for unittest
        """

        test = self.aritmetic.modulus((32, 517))
        resolve = 165.44

        self.assertEqual(test, resolve)

    def test_floor_division(self):
        """
        floor_division() test for unittest
        """

        test = self.aritmetic.floor_division((9, 3))
        resolve = 3.0

        self.assertEqual(test, resolve)


if __name__ == '__main__':
    unittest.main()
