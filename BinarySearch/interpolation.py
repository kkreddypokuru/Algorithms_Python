def search(bucket, low, high, y):
    # logging.info("\n ele %s \n low %s \n high %s \n----", bucket, low, high)
    if high >= low and bucket[low] <= y <= bucket[high]:
        x = low + (y - bucket[low]) * (high - low) // (bucket[high] - bucket[low])
        if bucket[x] == y:
            return x
        if y > bucket[x]:
            search(bucket, x + 1, high)
        else:
            search(bucket, 0, x - 1)
        pass
    return -1

