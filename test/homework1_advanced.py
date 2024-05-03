def count_occurrences(input1, input2, case_sensitive=True):
    if not case_sensitive:
        input1 = input1.lower()
        input2 = input2.lower()
    return input1.count(input2)

import unittest

class TestCountOccurrences(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(count_occurrences("cucumber", "u"), 2)
        self.assertEqual(count_occurrences("cucumber", "x"), 0)
        self.assertEqual(count_occurrences("Cucumber", "c"), 1)

    def test_case_sensitivity(self):
        self.assertEqual(count_occurrences("cucumber", "U", False), 2)
        self.assertEqual(count_occurrences("Cucumber", "c", False), 2)
        self.assertEqual(count_occurrences("Cucumber", "Uc", False), 1)
if __name__ == "__main__":
    unittest.main()