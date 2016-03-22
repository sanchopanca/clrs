def merge(a, b):
    """
    :param a: the first list to merge
    :param b: the second list to merge
    :return: merged list
    """
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if i < len(a):
        result.extend(a[i:])
    elif j < len(b):
        result.extend(b[j:])
    return result
