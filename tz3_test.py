import unittest
import tz3


class TestTZ3(unittest.TestCase):
    def test_min(self):
        self.assertEqual(tz3._min([1, 4, 2, 3]), 1)

    def test_max(self):
        self.assertEqual(tz3._max([1, 4, 2, 3]), 4)

    def test_sum(self):
        self.assertEqual(tz3._sum([1, 4, 2, 3]), 10)

    def test_prod(self):
        self.assertEqual(tz3._prod([1, 4, 2, 3]), 24)

    def test_read_file(self):
        self.assertEqual(tz3.read_file('data.txt'), [1, 4, 2, 3])


if __name__ == '__main__':
    unittest.main()
