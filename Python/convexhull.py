from functools import reduce
from math import sqrt
import operator
import pygal # pip install pygal
import random

#def dotProduct(vector1, vector2):
#    return reduce(operator.add, map(operator.mul, vector1, vector2))

# Z - of cross product of vectors (P1,P2 and P1,P3)
        # if 0, coliniear, +, left turn, -, right turn
def crossproduct(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])) - ((b[1] - a[1]) * (c[0] - a[0]))

def main(argv=None):
    points = []

    count = 20
    size = 100.0
    # Generate some random points.
    for i in range(1, count):
        points.append((random.uniform(0.0, size), random.uniform(0.0, size)))

    points = sorted(set(points))
    # Find the middle Y
    middle = sum(y for x,y in points) / count

    lower = []
    upper = []

    for point in points:
        while len(lower) > 1 and crossproduct(lower[-2], lower[-1], point) <= 0:
            lower.remove(lower[-1])
        lower.append(point)

    for point in reversed(points):
        while len(upper) > 1 and crossproduct(upper[-2], upper[-1], point) <= 0:
            upper.remove(upper[-1])
        upper.append(point)

    lower.remove(lower[-1])
    upper.remove(upper[-1])
    ch = lower + upper

    # Remove hull points from original array for rendering.
    inside = sorted(set([p for p in points if not(p in ch)]))

    xychart = pygal.XY()
    xychart.title = 'Convex Hull'
    xychart.add('hull', ch)
    xychart.add('points', inside)
    xychart.render_to_file('convexhull.svg')
    # Group both sides
    # Find the convex hull
#    points.sort()
#    smallest = points[0]
#    bydot = sorted(points, key=lambda x: dotProduct(smallest, x))
#    print (bydot)

if __name__ == '__main__':
    main()
