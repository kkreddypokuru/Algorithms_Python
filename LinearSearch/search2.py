# Time complexity O(n)
import logging
import timeit

logging.basicConfig(level=logging.INFO)


def search(array, element):
    total = len(array)
    mid = int(total / 2)
    print(array[mid])
    if array[mid] == element:
        return mid
    if array[mid] > element:
        return search(array[mid:total - 1], element)
    if array[mid] < element:
        return search(array[0: mid - 1], element)
    return None


def main():
    bucket = [10, 2, 5, 1, 15, 4]
    element = 5

    position = search(bucket, element)
    if position:
        logging.info("Search element %s found at position %s", element, position)
    else:
        logging.warning("Search element % not found", element)


main()
