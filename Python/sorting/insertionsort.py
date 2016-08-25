
def insertionSort(input):
    for i in range(1, len(input)-1):
        for j in range(i-1, 0, -1):
            if input[i] < input[j]:
                temp = input[j]
                input[j] = input[i]
                input[i] = temp

def main(argv=None):
    print(insertionSort(range(10, 0, -1)))


if __name__ == '__main__':
    main()
