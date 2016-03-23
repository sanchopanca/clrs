def merge(a, left, pivot, right):
    """
    :param a: the list
    :param left: left edge (including)
    :param pivot: the pivot
    :param right: right edge (excluding)
    """
    first = a[left:pivot]
    second = a[pivot:right]
    i, j = 0, 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            a[left + i + j] = first[i]
            i += 1
        else:
            a[left + i + j] = second[j]
            j += 1
    if i < len(first):
        for k in range(i, len(first)):
            a[left + k + j] = first[k]
    elif j < len(second):
        for k in range(j, len(second)):
            a[left + i + k] = second[k]
