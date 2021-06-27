import logging

logging.basicConfig(level=logging.INFO)


def search(items, lt, rt, element):
    if rt >= lt:
        mid = (lt + (
                    rt - lt) // 2)  # follow this formula to avoid ArrayIndexOutOfBoundException errors when higher
        # int sums
        if element == items[mid]:
            return mid + 1
        if element < items[mid]:
            return search(items, lt, mid - 1, element)
        else:
            return search(items, mid + 1, rt, element)
    else:
        return -1


# elements = random.sample(range(0, 100), 9)

allItems = [[1, 2, 3, 4], [1, 3], [2], [], [1, 4, 5, 6, 7, 3, 2]]
# allItems=[[1,3]]
item = 3
for elements in allItems:
    logging.info("elements %s", elements)
    elements.sort()
    pos = search(elements, 0, len(elements) - 1, item)
    if pos == -1:
        logging.warning("search element %s not found in elements", item)
    else:
        logging.info("search element %s found at positions %s in elements", item, pos)
