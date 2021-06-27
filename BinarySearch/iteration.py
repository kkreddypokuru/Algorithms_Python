from logging import basicConfig, INFO, info

basicConfig(level=INFO)


def search(values, lt, rt, sr):
    for ele in values:
        if lt >= rt:
            mid = (lt + rt - 1) // 2
            print(lt, rt, mid)
            if sr == values[mid]:
                return mid
            if sr > values[mid]:
                lt = mid + 1
            else:
                rt = mid - 1
        else:
            return -1


# elements = random.sample(range(0, 100), 9)
elements = [1, 2, 3, 4]
item = 3
info("elements %s", elements)
pos = search(elements, 0, len(elements) - 1, item)
info("search element found at %s", pos)
