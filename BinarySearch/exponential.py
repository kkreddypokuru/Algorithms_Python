from BinarySearch import iteration


def search(a, y):
    i = 1
    n = len(a)
    while i < n and y > a[i]:
        i = i*2
    return iteration.search(a, i // 2, min(i, n - 1), y)


def main(items, y):
    return search(items, y)
