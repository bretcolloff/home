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
    top = [p for p in points if p[1] > middle]
    bottom = [p for p in points if p[1] <= middle]
    lines = []
    for i in range(0, len(top) - 2):
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
            i += 1

        elif zcross < 1:
            lines.append((a, c))
            i += 1
        else:
            lines.append((a, b))

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
