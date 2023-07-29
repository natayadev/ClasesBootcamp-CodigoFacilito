""" Core Test file for Multi_Maths Package """
# __doc__ (Test file for testing modules and packages)

import unittest

from multi_maths.core import Core


class TestCore(unittest.TestCase):
    """
    Class for unittest Core
    """

    def setUp(self):
        """
        Instance the app()
        """
        self.core = Core()
        self.core.set_lang('en')
        self.core.set_response('digit')

    def test_ari_add(self):
        """
        Arithmetic addition for unittest
        """
        test = self.core.run('ari', 'add', (2, 3, 4))
        resolve = 9.0

        self.assertEqual(test, resolve)

    def test_ari_sub(self):
        """
        Arithmetic subtraction for unittest
        """
        test = self.core.run('ari', 'sub', (4, 3))
        resolve = 1.0

        self.assertEqual(test, resolve)

    def test_geo_ca(self):
        """
        Arithmetic addition for unittest
        """
        test = self.core.run('geo', 'ca', (4,))
        resolve = 50.26548245743669

        self.assertEqual(test, resolve)

    def test_geo_rp(self):
        """
        Arithmetic subtraction for unittest
        """
        test = self.core.run('geo', 'rp', (4, 2))
        resolve = 12.0

        self.assertEqual(test, resolve)

    def test_stat_sd(self):
        """
        Arithmetic addition for unittest
        """
        data_list = [8, 17, 41, 3, 21, 30, 11, 9]
        test = self.core.run('stat', 'sd', (data_list,))
        resolve = 12.739141034061687

        self.assertEqual(test, resolve)

    def test_stat_mode(self):
        """
        Arithmetic subtraction for unittest
        """
        data_list = [8, 17, 41, 3, 21, 30, 11, 9]
        test = self.core.run('stat', 'mode', (data_list,))
        resolve = 8.0

        self.assertEqual(test, resolve)


if __name__ == '__main__':
    unittest.main()
