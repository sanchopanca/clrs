def insertion_sort(a):
    """
    :param a: list which will be sorted in-place
    """
    if len(a) < 2:
        return
    for j in range(1, len(a)):
        i = j - 1
        while i >= 0 and a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            i -= 1


if __name__ == '__main__':
    import sys
    try:
        numbers = list(map(int, sys.argv[1:]))
        insertion_sort(numbers)
        print(numbers)
    except Exception as e:
        print(e)
        print('Usage:')
        print('python3 insertion_sort.py 7 2 0 ... 9')
