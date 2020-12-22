import unittest

from manager.rabin_karp import find_matches
from utils.read import read


class Tests(unittest.TestCase):

    def test(self):
        prime_number = 101
        text, pattern = read("../input1.txt")
        self.assertEqual(find_matches(text, pattern, prime_number), [6, 11])
        text, pattern = read("../input2.txt")
        self.assertEqual(find_matches(text, pattern, prime_number), [13, 23])


if __name__ == '__main__':
    unittest.main()
