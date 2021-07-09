import logging
import BinarySearch as bs
logging.basicConfig(level=logging.INFO)


def main():
    # allItems = [[8, 7, 6, 5, 4, 3, 2, 1, 0]]
    elements = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8],
        [1, 3],
        [2],
        [],
        [1, 4, 5, 6, 7, 3, 2]
    ]
    for items in elements:
        items.sort()
        y = 3
        pos = search(items, 0, len(items) - 1, y)
        if pos == -1:
            logging.warning("elements:%s, search:%s NOT FOUND", items, y)
        else:
            logging.info("elements:%s search:%s found at position:%s", items, y, pos)


if __name__ == '__main__':
    main()
