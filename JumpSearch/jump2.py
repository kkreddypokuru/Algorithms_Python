import logging
import math

logging.basicConfig(level=logging.INFO)


def search(a, n, x):
    p = 0
    b = int(math.sqrt(n))
    i = b
    while x > a[i-1]:
        p = i
        i = i + b
        if p >= n:
            return -1
    print('p:', p, 'i:', i)
    print(a[p])
    while x < a[p]:
        p = p + 1
        if p == i:
            return -1
    print('p:', p, 'i:', i)
    print(a[p])
    if x == a[p]:
        return p
    return -1


allItems = [[8, 7, 6, 5, 4, 3, 2, 1, 0]]
# allItems = [[0, 1, 2, 3, 4, 5, 6, 7, 8]]
# , [1, 3], [2], [], [1, 4, 5, 6, 7, 3, 2]]
item = 3
for elements in allItems:
    if elements:
        pos = search(elements, len(elements), item)
    else:
        pos = -1
    if pos == -1:
        logging.warning("elements:%s, search:%s NOT FOUND", elements, item)
    else:
        logging.info("elements:%s search:%s found at position:%s", elements, item, pos)
