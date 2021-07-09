import logging
import math

logging.basicConfig(level=logging.INFO)


def interpolation(bucket, low, high, y):
    # logging.info("\n ele %s \n low %s \n high %s \n----", bucket, low, high)
    if high >= low and bucket[low] <= y <= bucket[high]:
        x = low + (y - bucket[low]) * (high - low) // (bucket[high] - bucket[low])
        if bucket[x] == y:
            return x
        if y > bucket[x]:
            interpolation(bucket, x + 1, high)
        else:
            interpolation(bucket, 0, x - 1)
        pass
    return -1


# allItems = [[8, 7, 6, 5, 4, 3, 2, 1, 0]]
allItems = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [1, 3],
    [2],
    [],
    [1, 4, 5, 6, 7, 3, 2]
]

for items in allItems:
    items.sort()
    y = 3
    pos = interpolation(items, 0, len(items) - 1, y)
    if pos == -1:
        logging.warning("elements:%s, search:%s NOT FOUND", items, y)
    else:
        logging.info("elements:%s search:%s found at position:%s", items, y, pos)
