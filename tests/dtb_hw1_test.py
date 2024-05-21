import unittest


def count_occurrences(word, letter):
    count = 0

    start_index = 0

    while True:

        index = word.find(letter, start_index)

        if index == -1:
            break

        count += 1

        start_index = index + 1

    return count


def count_occurrences(word, letter, case_sensitive=True):
    count = 0

    if not case_sensitive:
        word = word.lower()

        letter = letter.lower()

    start_index = 0

    while True:

        index = word.find(letter, start_index)

        if index == -1:
            break

        count += 1

        start_index = index + 1

    return count


class TestCountOccurrences(unittest.TestCase):

    def test_occurrences(self):
        self.assertEqual(count_occurrences('cucumber', 'u'), 2)

        self.assertEqual(count_occurrences('cucumber', 'x'), 0)

        self.assertEqual(count_occurrences('Cucumber', 'c'), 1)

    def test_case_insensitive(self):
        self.assertEqual(count_occurrences('cucumber', 'U', case_sensitive=False), 2)

        self.assertEqual(count_occurrences('Cucumber', 'c', case_sensitive=False), 2)

        self.assertEqual(count_occurrences('Cucumber', 'Uc', case_sensitive=False), 1)


if __name__ == '__main__':
    unittest.main()