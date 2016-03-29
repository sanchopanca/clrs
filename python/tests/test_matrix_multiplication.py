import unittest

from matrix_multiplication import naive_matrix_multiplication, recursive_square_matrix_multiplication


class TestMatrixMultiplication(unittest.TestCase):
    def test_naive_multiplication(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        result = naive_matrix_multiplication(a, b)
        expected = [[19, 22], [43, 50]]
        for i in range(len(expected)):
            self.assertEqual(result[i], expected[i])

    def test_recursive_multiplication(self):
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        result = recursive_square_matrix_multiplication(a, b)
        expected = [[19, 22], [43, 50]]
        for i in range(len(expected)):
            self.assertEqual(result[i], expected[i])
