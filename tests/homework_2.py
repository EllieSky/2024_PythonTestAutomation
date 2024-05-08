import unittest

def count_occurrences(str, search, case_sensitive=True):
    if not case_sensitive:
        str = str.lower()
        search = search.lower()
    return str.count(search)

class Count(unittest.TestCase):
    def test_occurrences(self):
        self.assertEqual(count_occurrences("cucumber", "u"), 2)
        self.assertEqual(count_occurrences("cucumber", "x"), 0)
        self.assertEqual(count_occurrences("Cucumber", "c"), 1)

    def test_occurrences_case_sensitive(self):
        self.assertEqual(count_occurrences("cucumber", "U", False), 0)
        self.assertEqual(count_occurrences("Cucumber", "c", False), 2)
        self.assertEqual(count_occurrences("Cucumber", "Uc", False), 1)


if __name__ == "__main__":
    unittest.main()