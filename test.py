"""
Модуль для тестирования
"""

import os.path
import unittest

import main


class Test(unittest.TestCase):
    def test_load(self):
        self.assertEqual(main.load('templates/test_template.txt'),
                         ['Apple', 'Pear', 'Orange'])

    def test_failed_load(self):
        self.assertNotEqual(main.load('templates/no_file.txt'),
                            ['A', 'B', 'C'])

    def test_generate(self):
        main.generate('test.txt')
        self.assertEqual(os.path.isfile('../../../PycharmProjects/python_sandbox/name_generator/test.txt'), True)


if __name__ == '__main__':
    unittest.main()
