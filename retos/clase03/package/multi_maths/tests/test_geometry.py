""" Geometry Test file for Multi_Maths Package """
# __doc__ (Geometry Test file for testing modules and packages)

import configparser
from importlib.resources import files
import unittest

from multi_maths.mm_geometry.mm_geometry import MM_Geometry


class TestGeometry(unittest.TestCase):
    """
    Class for unittest Geometry
    """

    def setUp(self):
        """
        Instance the MM_Geometry()
        """

        lang_file = files("multi_maths").joinpath('languages/en.ini')  # noqa: E501  # pylint: disable=C0301
        self.lang = configparser.ConfigParser()
        self.lang.sections()
        self.lang.read(lang_file, 'UTF-8')

        self.geometry = MM_Geometry(self.lang, 'digit')

    def test_circle_circumference(self):
        """
        circle_circumference() test for unittest
        """

        test = self.geometry.circle_circumference(5.0)
        resolve = 31.41592653589793

        self.assertEqual(test, resolve)

    def test_square_perimeter(self):
        """
        square_perimeter() test for unittest
        """

        test = self.geometry.square_perimeter((5,))
        resolve = 20.0

        self.assertEqual(test, resolve)

    def test_parallelogram_area(self):
        """
        parallelogram_area() test for unittest
        """

        test = self.geometry.parallelogram_area((4, 3))
        resolve = 12.0

        self.assertEqual(test, resolve)


if __name__ == '__main__':
    unittest.main()
