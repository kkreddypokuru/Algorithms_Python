from logging import basicConfig, INFO, info, warning

basicConfig(level=INFO)


def search(values, lt, rt, sr):
    while lt<=rt:
        if rt >= lt:
            mid = (lt + (rt - lt) // 2)
            if sr == values[mid]:
                return mid+1
            if sr < values[mid]:
                rt = mid - 1
            else:
                lt = mid + 1
    return -1


# elements = random.sample(range(0, 100), 9)
allItems = [[1, 2, 3, 4], [1, 3], [2], [], [1, 4, 5, 6, 7, 3, 2]]
item = 5
for elements in allItems:
    elements.sort()
    pos = search(elements, 0, len(elements) - 1, item)
    if pos == -1:
        warning("search element %s not found in elements", item)
    else:
        info("elements:%s search:%s found at position:%s",elements, item, pos)

