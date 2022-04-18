import unittest
from tester import TestApp


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestApp('testCreateApp'))
    suite.addTest(TestApp('test_update'))
    return suite


if __name__ == '__main__':
    app = unittest.TextTestRunner()
    app.run(suite())