import unittest
from ramya_work_1 import count_occ
from ramya_work_1 import counting_occ_adv
from ramya_work_1 import counting_occ_expert


class TestCountOcc(unittest.TestCase):
    def test_count_occ(self):
        self.assertEqual(count_occ("Cucumber", "u"), 2)

    def test_count_occ_adv(self):
        self.assertEqual(counting_occ_adv("Cucumber", "c",False), 2)

    def test_counting_occ_expert(self):
        self.assertEqual(counting_occ_expert("The boy is 5 years old", "5"), 1)




if __name__ == '__main__':
    unittest.main()

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
