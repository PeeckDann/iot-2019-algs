import unittest

from manager.word_counter import final_count
from utils.read import read


class Tests(unittest.TestCase):

    def test(self):
        words = read("../wchain1.in")
        self.assertEqual(final_count(sorted(words, key=len), {}), 6)
        words = read("../wchain2.in")
        self.assertEqual(final_count(sorted(words, key=len), {}), 4)
        words = read("../wchain3.in")
        self.assertEqual(final_count(sorted(words, key=len), {}), 1)
        words = read("../wchain4.in")
        self.assertEqual(final_count(sorted(words, key=len), {}), 7)


if __name__ == '__main__':
    unittest.main()
