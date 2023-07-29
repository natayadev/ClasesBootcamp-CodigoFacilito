""" Statistics Test file for Multi_Maths Package """
# __doc__ (Statistics Test file for testing modules and packages)

import configparser
from importlib.resources import files
import unittest

from multi_maths.mm_statistics.mm_statistics import MM_Statistics


class TestStatistics(unittest.TestCase):
    """
    Class for unittest Statistics
    """

    def setUp(self):
        """
        Instance the MM_Statistics()
        """

        lang_file = files("multi_maths").joinpath('languages/en.ini')  # noqa: E501  # pylint: disable=C0301
        self.lang = configparser.ConfigParser()
        self.lang.sections()
        self.lang.read(lang_file, 'UTF-8')

        self.statistics = MM_Statistics(self.lang, 'digit')
        self.data_list = [8, 17, 41, 3, 21, 30, 11, 9]

    def test_standard_deviation(self):
        """
        standard_deviation() test for unittest
        """

        test = self.statistics.standard_deviation(self.data_list, 7)
        resolve = 16.978978599601163

        self.assertEqual(test, resolve)

    def test_mean(self):
        """
        mean() test for unittest
        """

        test = self.statistics.mean(self.data_list)
        resolve = 17.5

        self.assertEqual(test, resolve)

    def test_median(self):
        """
        median() test for unittest
        """

        test = self.statistics.median(self.data_list)
        resolve = 14.0

        self.assertEqual(test, resolve)


if __name__ == '__main__':
    unittest.main()
