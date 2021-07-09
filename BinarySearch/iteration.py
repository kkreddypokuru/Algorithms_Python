def search(values, lt, rt, sr):
    while lt <= rt:
        if rt >= lt:
            mid = (lt + (rt - lt) // 2)
            if sr == values[mid]:
                return mid + 1
            if sr < values[mid]:
                rt = mid - 1
            else:
                lt = mid + 1
    return -1
