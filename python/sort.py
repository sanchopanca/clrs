from utils import merge


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


def merge_sort(a):
    """
    :param a: list which will be sorted in-place
    """
    def _merge_sort(a, left, right):
        if right - left < 2:
            return
        pivot = (right + left) // 2
        _merge_sort(a, left, pivot)
        _merge_sort(a, pivot, right)
        merge(a, left, pivot, right)

    _merge_sort(a, 0, len(a))

if __name__ == '__main__':
    import sys
    try:
        sort_method = sys.argv[1]
        numbers = list(map(int, sys.argv[2:]))
        if sort_method == 'insertion_sort':
            insertion_sort(numbers)
            print(numbers)
        elif sort_method == 'merge_sort':
            print(merge_sort(numbers))
        else:
            raise Exception('Invalid argument %s' % sort_method)
    except Exception as e:
        print(e)
        print('Usage:')
        print('python3 sort.py <sort_method> 7 2 0 ... 9')
        print('Sort methods are "insertion_sort", "merge_sort"')
