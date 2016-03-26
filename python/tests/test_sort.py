import random
import unittest

import sort
import utils


class TestSort(unittest.TestCase):
    def setUp(self):
        random.seed('CLRS')

    def test_insertion_sort_random(self):
        for i in range(101):
            a = []
            for _ in range(i):
                a.append(random.randint(1, 10000))
            s = sorted(a)
            sort.insertion_sort(a)
            self.assertEqual(a, s)

    def test_merge_sort_random(self):
        for i in range(4):
            a = []
            for _ in range(i):
                a.append(random.randint(1, 10000))
            s = sorted(a)
            sort.merge_sort(a)
            self.assertEqual(a, s)

    def test_merge(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8]
        utils.merge(l, 0, 4, 8)
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(l, expected)

        l = []
        utils.merge(l, 0, 0, 0)
        expected = []
        self.assertEqual(l, expected)

        l = [1, 2, 3]
        utils.merge(l, 0, 3, 3)
        expected = [1, 2, 3]
        self.assertEqual(l, expected)

        l = [1, 2, 3]
        utils.merge(l, 0, 0, 3)
        expected = [1, 2, 3]
        self.assertEqual(l, expected)

        l = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
        utils.merge(l, 0, 5, 10)
        expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(l, expected)

        l = [1, 4, 9, 8]
        utils.merge(l, 0, 3, 4)
        expected = [1, 4, 8, 9]
        self.assertEqual(l, expected)
