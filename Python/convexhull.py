from functools import reduce
from math import sqrt
import operator
import random

#def dotProduct(vector1, vector2):
#    return reduce(operator.add, map(operator.mul, vector1, vector2))

def main(argv=None):
    points = []

    count = 20
    size = 10.0
    # Generate some random points.
    for i in range(1, count):
        points.append((random.uniform(0.0, size), random.uniform(0.0, size)))

    # Find the middle Y
    middle = sum(y for x,y in points) / count

    #Split the points
    #top = sorted([p for p in points if p[1] > middle], key=lambda x: x[0])
    top = [(0.6637461455718785, 6.247109561516067), (1.484270514375422, 7.717968957467511), (1.7642448293150836, 9.630483599941682), (2.9903533889165113, 9.332790899459754), (4.20799194695063, 9.15171082847384), (4.600751073006984, 7.595420538537139), (5.669572149435239, 8.82998085959816),(8.0, 8.0), (8.902037645352546, 5.8274526234967965)]
    bottom = sorted([p for p in points if p[1] <= middle], key=lambda x: x[1])
    lines = []
    i = 0
    while i < len(top) - 1:
        if i == len(top) - 2:
            lines.append((top[i], top[i+1]))
            i+=1
            continue
        a = top[i]
        b = top[i+1]
        c = top[i+2]

        # Z - of cross product of vectors (P1,P2 and P1,P3)
        # if 0, coliniear, +, left turn, -, right turn
        zcross = ((b[0] - a[0]) * (c[1] - a[1])) - ((b[1] - a[1]) * (c[0] - a[0]))
        if zcross == 0:
            lines.append((a, b))
            lines.append((b, c))
            # Jump ahead 1
            i += 2

        elif zcross > 0:
            lines.append((a, c))
            i += 2
        else:
            lines.append((a, b))
            i += 1

    print (top)
    print ("---lines---")
    print (lines)
    print ("complete")
    # Group both sides
    # Find the convex hull
#    points.sort()
#    smallest = points[0]
#    bydot = sorted(points, key=lambda x: dotProduct(smallest, x))
#    print (bydot)

if __name__ == '__main__':
    main()
