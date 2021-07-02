import logging
import math

logging.basicConfig(level=logging.INFO)


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


allItems = [[1, 2, 3, 4]]
# , [1, 3], [2], [], [1, 4, 5, 6, 7, 3, 2]]
item = 3
for elements in allItems:
    elements.sort()
    if elements:
        pos = search(elements, len(elements), item)
    else:
        pos = -1
    if pos == -1:
        logging.warning("elements:%s, search:%s NOT FOUND", elements, item)
    else:
        logging.info("elements:%s search:%s found at position:%s", elements, item, pos)
