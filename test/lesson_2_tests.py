import unittest

def sum_numbers(num1, num2):
    result = num1 + num2
    return result

class TestCalculator(unittest.TestCase):
    def test_example(self):
        # 2 ways possible to assert:
        self.assertNotEqual(True, False)
        self.assertNotEqual(True, True)

    def test_add_int_numbers(self):
        actual = sum_numbers(66, 71)  # Assign the result of sum_numbers to actual
        expected = 137
        self.assertEqual(expected, actual)

    def test_add_decimal_numbers(self):
        actual = sum_numbers(11.2, 4)  # Assign the result of sum_numbers to actual
        self.assertEqual(15.2, actual)

if __name__ == '__main__':
    unittest.main()