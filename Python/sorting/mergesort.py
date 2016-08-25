# Merge Sort
def mergeSort(input):
    if len(input) == 1:
        return input

    def merge(left, right):
        result = []

        while left and right:
            if left[0] <= right[0]:
                result.append(left[0])
                del left[0]
            else:
                result.append(right[0])
                del right[0]

        # One of the lists is empty, add the rest to the end.
        while left:
            result.append(left[0])
            del left[0]
        while right:
            result.append(right[0])
            del right[0]

        return result

    left = []
    right = []

    # Even numbers to right, odd numbers to left.
    for i, x in enumerate(input):
        if i % 2 == 0: right.append(x)
        else: left.append(x)

    # Subdivide again
    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

# Main
def main(argv=None):
    print (mergeSort([9,8,7,6,5,4,3,2,1]))

if __name__ == '__main__':
    main()
