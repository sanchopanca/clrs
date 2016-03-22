import random
import unittest

import insertion_sort
import utils


class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        random.seed('CLRS')

    def test_insertion_sort_random(self):
        for i in range(101):
            a = []
            for _ in range(i):
                a.append(random.randint(1, 10000))
            s = sorted(a)
            insertion_sort.insertion_sort(a)
            self.assertEqual(a, s)

    def test_merge(self):
        merged = utils.merge([1, 2, 3, 4], [5, 6, 7, 8])
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(merged, expected)

        merged = utils.merge([], [])
        expected = []
        self.assertEqual(merged, expected)

        merged = utils.merge([1, 2, 3], [])
        expected = [1, 2, 3]
        self.assertEqual(merged, expected)

        merged = utils.merge([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(merged, expected)

        merged = utils.merge([1, 3, 5, 7, 9], [0, 2, 4, 6, 8])
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(merged, expected)

        merged = utils.merge([1, 4, 9], [8])
        expected = [1, 4, 8, 9]
        self.assertEqual(merged, expected)
