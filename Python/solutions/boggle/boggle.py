import os, sys
lib_path = os.path.abspath(os.path.join('..', '..'))
sys.path.append(lib_path)
import random
import string
import time
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
    size = 20
    for i in range(0,size):
        line = []
        for j in range(0, size):
            line.append(random.choice(string.ascii_uppercase))

        board.append(line)

    routes = []
    checklist = []
    words = []

    start = time.time()

    # Starting from each point
    for i in range(0, size):
        for j in range(0, size):
            routes.append([(i, j)])

    # While there are still routes to evaluate, expand and evaluate.
    while routes:
        for route in list(routes):
            s = ''.join([board[x][y] for (x,y) in route])
            (exists, word) = t.lookup(s)
            if not exists:
                routes.remove(route)
                if not routes:
                    break
                continue

            if word:
                #print (s, " - ", route)
                words.append(s)

            (x, y) = route[-1]
            up = (x, y-1)
            down = (x, y+1)
            left = (x-1, y)
            right = (x+1, y)

            ur = (x+1, y-1)
            dr = (x+1, y+1)
            ul = (x-1, y-1)
            dl = (x-1, y+1)

            #for n in range(-1, 1):
            #    for m in range(-1, 1):
            #        n = n + x
            #        m = m + y
            #        point = (n, m)
            #        if n >= 0 and n < size and m >= 0 < m < size and point not in route:
            #            routes.append(route + [point])

            if x > 0 and left not in route:
                routes.append(route + [left])
            if x < size - 1 and right not in route:
                routes.append(route + [right])
            if y > 0 and up not in route:
                routes.append(route + [up])
            if y < size - 1 and down not in route:
                routes.append(route + [down])

            if x > 0 and y > 0 and ul not in route:
                routes.append(route + [ul])
            if x > 0 and y < size - 1 and dl not in route:
                routes.append(route + [dl])
            if x < size - 1 and y > 0 and ur not in route:
                routes.append(route + [ur])
            if x < size - 1 and y < size - 1 and dr not in route:
                routes.append(route + [dr])
            routes.remove(route)
            if not routes:
                break

    end = time.time()
    wordset = set(words)
    for word in wordset:
        print (word)

    print ("Finished in ", end - start, "seconds.")

    print("finished")
if __name__ == '__main__':
  main()
