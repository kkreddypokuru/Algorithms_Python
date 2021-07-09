import Sorting.selection
import logging

logging.basicConfig(level=logging.INFO)


def main(f):
    elements = [
        [],
        [1],
        [10, 2],
        [-1, 10, 2],
        [-1],
        [-1, 1, 0],
        [4, 2, 10]
    ]
    for ele in elements:
        beforeSort = ele.copy()
        sortedEle = f(ele)
        logging.info("sorted ele:%s, before sort ele:%s", sortedEle, beforeSort)


if __name__ == '__main__':
    f = Sorting.selection.sorting
    main(f)