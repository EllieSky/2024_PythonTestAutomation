import unittest

def count_occur(input1, input2, case_sensitive=True):
    if not case_sensitive:
        input1 = input1.lower()
        input2 = input2.lower()
    return input1.count(input2)


class TestCount(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_basic_level(self):
        self.assertEqual(count_occur("cucumber","u"),2)
    def test_basic_level_1(self):
        self.assertEqual(count_occur("cucumber", "x"),0)
    def test_basic_level_2(self):
        self.assertEqual(count_occur("Cucumber", "c"),1)

    def test_advanced_level(self):
        self.assertEqual(count_occur("cucumber", "U", False), 2)

    def test_advanced_level_1(self):
        self.assertEqual(count_occur("Cucumber", "c", False), 2)
    def test_advanced_level_2(self):
        self.assertEqual(count_occur("Cucumber", "Uc", False), 1)

    # def test_expert_level(self):
    #     self.assertEqual(count_occur("The boy was 5 years old", 5), 1)
    #
    # def test_expert_level_1(self):
    #     self.assertEqual(count_occur(60224012, 2), 3)
    #
    # def test_expert_level_2(self):
    #     self.assertEqual(count_occur(60224012, "12"), 1)





if __name__ == '__main__':
    unittest.main()
