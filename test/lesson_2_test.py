import unittest
# imporatant in unittest'h
def sum_numbers(num1, num2, num3=0.0):
    result = num1 + num2 + num3
    return result



class TestCalculator(unittest.TestCase):
    def test_example(self):
        self.assertNotEqual(True, False) # add assertion here
        self.assertEqual(True,True)

    def test_add_int_numbers(self):
           actual = sum_numbers(66, 71)
           expected = 137
           self.assertEqual(expected, actual)
    def test_add_decimal_numbers(self):
        self.assertEqual(15.2,  sum_numbers(11.2,4))

    def test_add_3_numbers(self):
        self.assertEqual(10, sum_numbers(5, 3.5,1.5 ))


if __name__ == '__main__':
    unittest.main()
