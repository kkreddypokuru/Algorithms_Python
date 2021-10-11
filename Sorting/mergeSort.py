import logging

logging.basicConfig(level=logging.INFO)


def splitArray(array):
    if len(array)>1:
        mid = len(array) // 2
        leftArray = array[:mid]
        rightArray = array[mid:]
        print("left Array-->", leftArray)
        splitArray(leftArray,)
        print("right Array-->", rightArray)
        splitArray(rightArray)
        mergeArray(leftArray, rightArray)

def mergeArray(l, r):
    if len(l) == 1 and len(r) ==1:
        return l+r
    else:
        while

a = [5, 3, 2, 1, 6]

splitArray(a)
