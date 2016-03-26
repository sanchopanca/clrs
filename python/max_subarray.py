def _find_max_crossing_subarray(a, left, middle, right):
    left_index = middle-1
    left_sum = -float('inf')
    s = 0
    for i in range(middle-1, left-1, -1):
        s += a[i]
        if s > left_sum:
            left_sum = s
            left_index = i
    s = 0
    right_index = middle
    right_sum = -float('inf')
    for i in range(middle, right):
        s += a[i]
        if s > right_sum:
            right_sum = s
            right_index = i
    return left_index, right_index, left_sum + right_sum


def _find_max_subarray(a, left, right):
    if right - left == 1:
        return left, left, a[left]
    middle = (left + right) // 2
    left_from, left_to, left_sum = _find_max_subarray(a, left, middle)
    right_from, right_to, right_sum = _find_max_subarray(a, middle, right)
    crossing_from, crossing_to, crossing_sum = _find_max_crossing_subarray(a, left, middle, right)
    if left_sum >= right_sum and left_sum >= crossing_sum:
        return left_from, left_to, left_sum
    elif right_sum >= crossing_sum:
        return right_from, right_to, right_sum
    return crossing_from, crossing_to, crossing_sum


def find_max_subarray(a):
    """
    :param a: list
    :return: left index, right_index, sum
    """
    if not a:
        raise ValueError("Array must contain at least one item")
    return _find_max_subarray(a, 0, len(a))


if __name__ == '__main__':
    import sys
    try:
        numbers = list(map(int, sys.argv[1:]))
        print('left_index={}, right_index={}, sum={}'.format(*find_max_subarray(numbers)))
    except Exception as e:
        print(e)
        print('Usage:')
        print('python3 max_subarray.py <numbers>')
