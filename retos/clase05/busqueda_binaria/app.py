""" Main file for BinarySearchAlgorithms"""
# __doc__ (Main file for little data structure app testing
# Binary Search Algorithms)

from app.controllers.default import DefaultController


if __name__ == '__main__':
    app = DefaultController()
    app.create_app()
    app.show_credits(True)
