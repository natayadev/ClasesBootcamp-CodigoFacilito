""" Main file for Recital """
# __doc__ (Main file for little Recital app for testing
# Queues and Piles)

from app.controllers.default import DefaultController


if __name__ == '__main__':
    app = DefaultController()
    app.create_app()
    print('', end='')
    app.show_credits(True)
