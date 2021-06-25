# Time Complexity is O(n)

import logging
import timeit
logging.basicConfig(level=logging.INFO)


def linear(array, search):
    for index in range(0, len(array) - 1):
        if array[index] == search:
            return True, index
    return False, -1


def main():
    bucket = [10, 2, 5, 1, 15, 4]
    element = 5

    found, position = linear(bucket, element)
    if found:
        logging.info("Search element %s found at position %s", element, position)
    else:
        logging.warning("Search element % not found", element)


main()
