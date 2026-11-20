import unittest

from sonar_dummy_python_oss.example import is_even


class IsEvenTest(unittest.TestCase):
    def test_integer_parity(self):
        for number, expected in ((2, True), (3, False), (0, True), (-2, True), (-3, False)):
            with self.subTest(number=number):
                self.assertIs(is_even(number), expected)
