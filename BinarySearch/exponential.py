import math


def search(a, y):
    inc = 0
    i = int(math.pow(2, inc))
    n = len(a)
    while i <= n - 1 and y < a[i]:
        inc = inc + 1
        i = int(math.pow(2, inc))
    print(i, a[i])
    return search(a, i / 2, min(i, n - 1), y)
