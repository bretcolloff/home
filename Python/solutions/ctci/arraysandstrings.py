
# Implement an algorithm to determine if a string has all unique characeters.
def onepointone(input):
    print("1.1")
    print(len(set(input)))

    # What if you cannot use additional data structures?
    total = 0
    lastletter = ''
    for letter in sorted(input):
        if letter != lastletter:
            lastletter = letter
            total += 1
    print (total)

def onepointtwo():
    print("1.2")
    print("Walk a point to the end, start one at the start. Swap")

# Given two strings, write a method to decide if one is a permutation of the other.
def onepointthree(a, b):
    print("1.3")
    if len(a) != len (b):
        return False
    a = sorted(a)
    b = sorted(b)
    result = True
    for i in range(0, len(a)):
        if a[i] != b[i]:
            result = False
            break
    print (result)

# Replace spaces with %20s
def onepointfour(input):
    print("1.4")
    input = list(input)
    lastcharacter = len(input) - 1
    lastindex = len(input) - 1
    start = 0

    while True:
        if input[lastcharacter] != ' ':
            break
        lastcharacter -= 1

    while True:
        if input[start] is not ' ':
            start += 1
        else:
            start -= 1
            break

    # Walk backwards and keep pushing the characters to the end.
    while lastcharacter > start:
        if input[lastcharacter] is not ' ':
            input[lastindex] = input[lastcharacter]
            input[lastcharacter] = ' '
            lastcharacter -= 1
            lastindex -= 1
        else:
            lastcharacter -= 1
            lastindex -= 3

    # Replace the spaces with 'spaces'
    for i in range(0, len(input) - 1):
        if input[i] == ' ':
            input[i] = '%'
            input[i + 1] = '2'
            input[i + 2] = '0'
            i += 3
    print (''.join(input))

# String compression
def onepointfive(input):
    print("1.5")

    output = []
    outputlen = 0
    lastchar = ''
    count = 0
    compressed = True
    for i, c in enumerate(list(input)):
        if c is not lastchar:
            if lastchar is '':
                lastchar = c
                count = 1
                continue
            output.append(str(lastchar))
            output.append(str(count))
            outputlen += 2
            count = 0
            lastchar = c
            count += 1
        else:
            count += 1

        if outputlen > i:
            compressed = False
            break

    output.append(str(lastchar))
    output.append(str(count))

    if compressed:
        print(''.join(output))
    else:
        print(input)

def onepointsix():
    print("1.6")

def onepointseven():
    print("1.7")

def onepointeight():
    print("1.8")

def main(argv=None):
    onepointone("abcdefggg")
    onepointtwo()
    onepointthree("abcde", "edcba")
    onepointfour("Mr John Smith    ")
    onepointfive("aabbcccccaaa")
    onepointsix()
    onepointseven()
    onepointeight()

if __name__ == '__main__':
    main()
