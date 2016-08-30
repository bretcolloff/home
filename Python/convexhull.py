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

    top = [(1.352876282020794, 8.684818995888326), (1.754226650542784, 9.470327874963996), (3.3051466695830376, 4.976302065179778), (3.9701121282171234, 5.5515319916907035), (4.698564132458127, 5.676323179175487), (5.057822789532183, 9.781881843793673), (5.185922021599975, 8.830708789449238), (6.847942969302534, 4.996067183490638), (6.968719524002818, 7.120484352330676), (7.468802601158143, 8.119374866962696)]
    bottom = [(4.47702275021607, 0.4931686439414473), (7.196698000758655, 1.1859965444347242), (7.199454144624892, 1.7334545504117738), (9.218249343842182, 2.2094661131873528), (4.790969604383234, 2.738820568012793), (1.6887520392984334, 3.2388367738180723), (7.223235024234473, 3.6903409363904682), (6.401934780753489, 3.9045557997554194), (3.2806010547084585, 4.4278343733701995)]
    #Split the points
    #top = sorted([p for p in points if p[1] > middle], key=lambda x: x[0])
    #top = [(0.6637461455718785, 6.247109561516067), (1.484270514375422, 7.717968957467511), (1.7642448293150836, 9.630483599941682), (2.9903533889165113, 9.332790899459754), (4.20799194695063, 9.15171082847384), (4.600751073006984, 7.595420538537139), (5.669572149435239, 8.82998085959816),(8.0, 8.0), (8.902037645352546, 5.8274526234967965)]
    #bottom = sorted([p for p in points if p[1] <= middle], key=lambda x: x[1])
    lines = []

    for x, l in enumerate([top, bottom]):
        i = 0
        while i < len(l) - 1:
            if i == len(l) - 2:
                lines.append((l[i], l[i+1]))
                i+=1
                continue
            a = l[i]
            b = l[i+1]
            c = l[i+2]

            # Z - of cross product of vectors (P1,P2 and P1,P3)
            # if 0, collinear, +, left turn, -, right turn
            zcross = ((b[0] - a[0]) * (c[1] - a[1])) - ((b[1] - a[1]) * (c[0] - a[0]))
            if x > 0:
                zcross = 0 - zcross

            if zcross == 0:
                lines.append((a, b))
                lines.append((b, c))
                # Jump ahead
                i += 2
            elif zcross > 0:
                lines.append((a, c))
                i += 2
            else:
                lines.append((a, b))
                i += 1

    print ("top:", top)
    print ("bottom:", bottom)
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
