""" Test file for BinarySearchAlgorithms"""
# __doc__ (Test file for little data structure app testing
# Binary Search Algorithms)

import unittest

from app.controllers.default import DefaultController


class TestBinarySearchAlgorithms(unittest.TestCase):
    """
    Class for unittest BinarySearchAlgorithms
    """

    def setUp(self):
        """
        Instance the app()
        """
        self.app = DefaultController()

    def test_credits(self):
        """
        Credits Test - Sory, I need more time to make some test for unittest
        """
        resolve = self.app.show_credits(False)
        title = 'Binary Search Algorithms'

        self.assertEqual(title, resolve['title'])


if __name__ == '__main__':
    unittest.main()
