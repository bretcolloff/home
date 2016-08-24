import string
import random
from lib.trie import Trie

#Pick a starting point.
#while(Problem is not solved)
#	For each path from the starting point.
#		check if selected path is safe, if yes select it
#                and make recursive call to rest of the problem
#		If recursive calls returns true, then return true.
#		else undo the current move and return false.
#	End For
#	If none of the move works out, return false, NO SOLUTON.

def main(argv=None):
    t = Trie()
    with open("dictionary.txt") as f:
      for line in f:
         t.insert(line.upper().replace('\n',''))

    # Generate board
    board = []
    for i in range(0,5):
        line = []
        for j in range(0, 5):
            line.append(random.choice(string.ascii_uppercase))

        board.append(line)

    routes = []
    checklist = []
    words = []

    # Starting from each point
    for i in range(0, 5):
        for j in range(0, 5):
            routes.append([(i, j)])

    # While there are still routes to evaluate, expand and evaluate.
    while routes:
        for route in list(routes):
            s = ''.join([board[x][y] for (x,y) in route])
            (exists, word) = t.lookup(s)
            if not exists:
                routes.remove(route)
                continue

            (x, y) = route[0]
            up = (x, y-1)
            down = (x, y+1)
            left = (x-1, y)
            right = (x+1, y)

            ur = (x+1, y-1)
            dr = (x+1, y+1)
            ul = (x-1, y-1)
            dl = (x-1, y+1)

            if x > 0 and left not in route:
                routes.append(route + [left])
            if x < 4 and right not in route:
                routes.append(route + [right])
            if y > 0 and up not in route:
                routes.append(route + [up])
            if y < 4 and down not in route:
                routes.append(route + [down])

            if x > 0 and y > 0 and ul not in route:
                routes.append(route + [ul])
            if x > 0 and y < 4 and dl not in route:
                routes.append(route + [dl])
            if x < 4 and y > 0 and ur not in route:
                routes.append(route + [ur])
            if x < 4 and y < 4 and dr not in route:
                routes.append(route + [dr])
            routes.remove(route)
            checklist.append(route)

    for route in checklist:
        s = ''.join([board[x][y] for (x,y) in route])
        if s in d:
            print(s)

    print("finished")
if __name__ == '__main__':
  main()
