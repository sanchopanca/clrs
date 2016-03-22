import random
import unittest

import insertion_sort


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
