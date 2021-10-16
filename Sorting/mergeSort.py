import logging

logging.basicConfig(level=logging.INFO)


def splitArray(array):
    if len(array) > 1:
        mid = len(array) // 2
        leftArray = array[:mid]
        rightArray = array[mid:]
        print("Split Step:", "array:", array, "-->", "left:", leftArray, "<-->", "right:", rightArray)
        splitArray(leftArray)
        splitArray(rightArray)
        print("merge Step:", "left:", leftArray, "<-->", "right:", rightArray)
        i = j = k = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                array[k] = leftArray[i]
                i += 1
            else:
                array[k] = rightArray[j]
                j += 1
            k += 1
        while i < len(leftArray):
            array[k] = leftArray[i]
            i += 1
            k += 1
        while j < len(rightArray):
            array[k] = rightArray[j]
            j += 1
            k += 1
        print("array:", array)
        return array


a = [5, 3, 2, 1, 6]
# a = [38, 27, 43, 3, 9, 82, 10]
print(a)
arr = splitArray(a)
print('arr---->', arr)
