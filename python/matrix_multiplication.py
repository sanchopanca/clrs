from utils import matrix_addition


def naive_matrix_multiplication(a, b):
    m = len(a)
    n = len(a[0])
    o = len(b)
    p = len(b[0])
    if n != o:
        raise ValueError('The number of columns in a must be equal to number of rows in b')
    result = []
    for i in range(m):
        result.append([0] * p)
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def recursive_square_matrix_multiplication(a, b):
    n = len(a)
    if not ((n == len(a[0]) and len(b) == len(b[0]) and n == len(b)) and (n & (n-1) == 0)):
        raise ValueError('a and b must be matrix n x n where n is a power of 2')

    def _recursive(a, b):
        if len(a) == 1:
            return [[a[0][0] * b[0][0]]]

        upper_left_a = a[:len(a) // 2]
        for i in range(len(upper_left_a)):
            upper_left_a[i] = a[i][:len(a[i]) // 2]

        upper_left_b = b[:len(b) // 2]
        for i in range(len(upper_left_b)):
            upper_left_b[i] = b[i][:len(b[i]) // 2]

        upper_right_a = a[:len(a) // 2]
        for i in range(len(upper_right_a)):
            upper_right_a[i] = a[i][len(a[i]) // 2:]

        upper_right_b = b[:len(b) // 2]
        for i in range(len(upper_right_b)):
            upper_right_b[i] = b[i][len(b[i]) // 2:]

        bottom_left_a = a[len(a) // 2:]
        for i in range(len(bottom_left_a)):
            bottom_left_a[i] = bottom_left_a[i][:len(bottom_left_a[i]) // 2]

        bottom_left_b = b[len(b) // 2:]
        for i in range(len(bottom_left_b)):
            bottom_left_b[i] = bottom_left_b[i][:len(bottom_left_b[i]) // 2]

        bottom_right_a = a[len(a) // 2:]
        for i in range(len(bottom_right_a)):
            bottom_right_a[i] = bottom_right_a[i][len(bottom_right_a[i]) // 2:]

        bottom_right_b = b[len(b) // 2:]
        for i in range(len(bottom_right_b)):
            bottom_right_b[i] = bottom_right_b[i][len(bottom_right_b[i]) // 2:]

        upper_left = matrix_addition(_recursive(upper_left_a, upper_left_b),
                                     _recursive(upper_right_a, bottom_left_b))
        upper_right = matrix_addition(_recursive(upper_left_a, upper_right_b),
                                      _recursive(upper_right_a, bottom_right_b))
        bottom_left = matrix_addition(_recursive(bottom_left_a, upper_left_b),
                                      _recursive(bottom_right_a, bottom_left_b))
        bottom_right = matrix_addition(_recursive(bottom_left_a, upper_right_b),
                                       _recursive(bottom_right_a, bottom_right_b))
        result = []
        for i in range(len(upper_left)):
            result.append(upper_left[i] + upper_right[i])
        for i in range(len(bottom_left)):
            result.append(bottom_left[i] + bottom_right[i])
        return result
    return _recursive(a, b)


if __name__ == '__main__':
    recursive_square_matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]])