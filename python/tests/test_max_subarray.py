import unittest

import max_subarray


class TestMaxSubarray(unittest.TestCase):
    def test_max_subarray(self):
        a = [1, 2, 3, 4, 5, 6]
        i, j, s = max_subarray.find_max_subarray(a)
        self.assertEqual(i, 0)
        self.assertEqual(j, len(a)-1)
        self.assertEqual(s, sum(a))

        a = [-1, 2, 3, -1]
        i, j, s = max_subarray.find_max_subarray(a)
        self.assertEqual(i, 1)
        self.assertEqual(j, 2)
        self.assertEqual(s, 5)
        
        a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        i, j, s = max_subarray.find_max_subarray(a)
        self.assertEqual(i, 7)
        self.assertEqual(j, 10)
        self.assertEqual(s, 43)
