import logging

logging.basicConfig(level=logging.INFO)


def search(items, lt, rt, element):
    if rt >= lt:
        mid = (lt + rt - 1) // 2
        if element == items[mid]:
            return mid
        if element < items[mid]:
            return search(items, lt, mid - 1, element)
        else:
            return search(items, mid + 1, rt, element)
    else:
        return -1


# elements = random.sample(range(0, 100), 9)
elements = [1, 2, 3, 4]
found = 3
logging.info("elements %s", elements)
left = 0
right = len(elements) - 1
pos = search(elements, left, right, found)
logging.info("search element found at %s", pos)
