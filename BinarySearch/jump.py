import math


def search(items, length, val):
    step = int(math.sqrt(length))
    prev = 0
    while val > items[min(step, length) - 1]:
        prev = step
        step = step + int(math.sqrt(length))
        if prev >= length:
            return -1
    print(prev, step)
    while val < items[prev]:
        prev = prev + 1
        if prev == min(step, length):
            return -1
    if items[prev] == val:
        return prev

    return -1
