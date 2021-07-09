import logging

import BinarySearch.exponential

logging.basicConfig(level=logging.INFO)


def main(callFun):
    elements = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8],
        [1, 3],
        [2],
        [],
        [1, 4, 5, 6, 7, 3, 2]
    ]
    searchingElement = 3
    for ele in elements:
        ele.sort()
        pos = callFun(ele, searchingElement)
        if pos == -1:
            logging.warning("searching element:%s NOT FOUND in elements:%s", searchingElement, ele)
        else:
            logging.info("searching element:%s found at position:%s in elements:%s", searchingElement, pos,  ele)


if __name__ == '__main__':
    func = BinarySearch.exponential.main
    main(func)
