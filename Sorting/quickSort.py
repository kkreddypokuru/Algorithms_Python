import logging

logging.basicConfig(level=logging.INFO)


def partition(array, start, end):
    p_idx = start
    p = array[p_idx]
    print('p -> array:', array)
    while start < end:
        while start < len(array) and array[start] <= p:
            start = start + 1
        while array[end] > p:
            end = end - 1
        if start < end:
            array[start], array[end] = array[end], array[start]
        print('while array:', array)
    array[end], array[p_idx] = array[p_idx], array[end]
    print('final return array:', array)
    return end


def quickSort(a, start, end):
    if start < end:
        p = partition(a, start, end)
        quickSort(a, start, p - 1)
        quickSort(a, p + 1, end)

    return a


# a = [5, 3, 2, 1, 6]
a = [38, 27, 43, 3, 9, 82, 10]
# end, array = partition(a, start=0, end=len(a) - 1)
array = quickSort(a, start=0, end=len(a) - 1)
print(array)
