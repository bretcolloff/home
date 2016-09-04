import os, sys
from itertools import islice

# def inversionmerge(input):
#     length = len(input)
#     if len(input) == 1:
#         return (0, input)
#
#     def merge(left, right):
#         resultl = []
#         resultc = 0
#
#         while left and right:
#             if left[0] <= right[0]:
#                 result.append(left[0])
#                 del left[0]
#             else:
#                 resultc = resultc + len(left)
#                 result.append(right[0])
#                 del right[0]
#
#         # One of the lists is empty, add the rest to the end.
#         while left:
#             result.append(left[0])
#             del left[0]
#         while right:
#             result.append(right[0])
#             del right[0]
#
#         return (resultc, resultl)
#
#     middle = int(length/2)-1
#     left = islice(input, 0, middle)
#     print (left)
#     right = islice(input, middle+1, length-1)
#     print (right)
#
#     # Subdivide again
#     left = inversionmerge(left)
#     right = inversionmerge(right)
#
#     return merge(left, right)
count = 0

def merge_sort(li, c):
    if len(li) < 2: return li
    m = len(li) / 2
    return merge(merge_sort(li[:int(m)],c), merge_sort(li[int(m):],c),c)

def merge(l, r, c):
    result = []
    l.reverse()
    r.reverse()
    while l and r:
        s = l if l[-1] < r[-1] else r
        result.append(s.pop())
        if (s == r): c[0] += len(l)
    rest = l if l else r
    rest.reverse()
    result.extend(rest)
    return result

def main(argv=None):
    unsorted = []
    with open("IntegerArray.txt") as f:
      for line in f:
         unsorted.append(int(line))

    count = [0]
    done = merge_sort(unsorted, count)
    print (count[0])
if __name__ == '__main__':
    main()
