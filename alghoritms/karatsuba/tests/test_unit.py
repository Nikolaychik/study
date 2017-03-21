import unittest
from funcs import make_one_length_vars, recursive_karatsuba


class TestFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_zeros_to_integer_if_needed(self):
        x, y = '1', '1234'
        resulted_x, resulted_y = make_one_length_vars(x, y)
        expected_x, expected_y = '0001', '1234'

        self.assertEqual(expected_x, resulted_x)
        self.assertEqual(expected_y, resulted_y)

    def test_recursive_karatsuba(self):
        x, y = 123430809839, 5678809890909
        result = recursive_karatsuba(x, y)
        expected_result = x*y
        self.assertEqual(result, expected_result)

    def test_failed_recursive_karatsuba(self):
        x, y = 123430809839, 'error'
        result = recursive_karatsuba(x, y)
        # expected_result = x*y
        # self.assertEqual(result, expected_result)

