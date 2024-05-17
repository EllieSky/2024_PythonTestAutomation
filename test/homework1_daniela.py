def count_occurrences(input1, input2):
    return input1.count(input2)

import unittest

class TestCountOccurrences(unittest.TestCase):
    def test_count_occurrences_u(self):
        self.assertEqual(count_occurrences("cucumber", "u"), 2)

    def test_count_occurrences_x(self):
        self.assertEqual(count_occurrences("cucumber", "x"), 0)

    def test_count_occurrences_c(self):
        self.assertEqual(count_occurrences("Cucumber", "c"), 1)

if __name__ == "__main__":
    unittest.main()