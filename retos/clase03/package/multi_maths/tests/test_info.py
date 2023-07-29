""" Test file for BinarySearchAlgorithms"""
# __doc__ (Test file for little data structure app testing
# Binary Search Algorithms)

import unittest

from multi_maths.info import Info


class TestInfo(unittest.TestCase):
    """
    Class for unittest Info
    """

    def setUp(self):
        """
        Instance the info()
        """
        self.info = Info()

    def test_credits(self):
        """
        Credits Test
        """
        resolve = self.info.show_credits(False)
        title = 'Multi Maths Package'

        self.assertEqual(title, resolve['title'])


if __name__ == '__main__':
    unittest.main()
