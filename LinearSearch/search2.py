# Python3 program for linear search
def search(arrayBucket, search_Element):
    left = 0
    length = len(arrayBucket)
    position = -1
    right = length - 1

    # Run loop from 0 to right
    for left in range(0, right, 1):

        # If search_element is found with
        # left variable
        if arrayBucket[left] == search_Element:
            position = left
            print("Element found in Array at ", position +
                  1, " Position with ", left + 1, " Attempt")
            break

        # If search_element is found with
        # right variable
        if arrayBucket[right] == search_Element:
            position = right
            print("Element found in Array at ", position + 1,
                  " Position with ", length - right, " Attempt")
            break
        # left += 1
        right -= 1
    # If element not found
    if position == -1:
        print("Not found in Array with ", left, " Attempt")


# Driver code
arr = [1, 2, 3, 4, 5]
search_element = 3

# Function call
search(arr, search_element)

# This code is contributed by Dharanendra L V.
