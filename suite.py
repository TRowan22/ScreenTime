import unittest
from tester import TestApp


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestApp('test_read_write'))
    suite.addTest(TestApp('test_add_app'))
    suite.addTest(TestApp('test_create_app'))
    # suite.addTest(TestApp('test_update'))
    suite.addTest(TestApp('test_convert_file'))
    suite.addTest(TestApp('test_find_current_path'))
    suite.addTest(TestApp('test_send_to_json'))
    suite.addTest(TestApp('test_get_names'))
    suite.addTest(TestApp('test_get_day_total'))
    suite.addTest(TestApp('test_get_week_total'))
    suite.addTest(TestApp('test_set_path'))
    return suite


if __name__ == '__main__':
    app = unittest.TextTestRunner()
    app.run(suite())